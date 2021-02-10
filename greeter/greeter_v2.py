from messages_pb2 import SeenCount, GreetRequest, GreetResponse, LastSeenTimestampMillis, Email

from statefun import StatefulFunctions
from statefun import StateSpec
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

import time

functions = StatefulFunctions()


@functions.bind(
    typename="com.foo.bar/greeter",
    states=[StateSpec('seen_count'), StateSpec('last_seen_timestamp')])
def greet(context, greet_request: GreetRequest):
    state = context.state('seen_count').unpack(SeenCount)
    if not state:
        state = SeenCount()
        state.seen = 1
    else:
        state.seen += 1
    context.state('seen_count').pack(state)

    last_seen = context.state('last_seen_timestamp').unpack(LastSeenTimestampMillis)
    response = compute_greeting(greet_request.name, state.seen, last_seen)

    now = LastSeenTimestampMillis()
    now.timestamp = time.time()
    context.state('last_seen_timestamp').pack(now)

    egress_message = kafka_egress_record(topic="greetings", key=greet_request.name, value=response)
    context.pack_and_send_egress("com.foo.bar/greets", egress_message)

    email = Email()
    email.recipient = greet_request.name
    context.pack_and_send("com.foo.bar/email_sender", email.recipient, email)


def compute_greeting(name, seen, last_seen):
    """
    Compute a personalized greeting, based on the number of times this @name had been seen before.
    """
    templates = ["", "Welcome %s.", "Nice to see you again %s.", "Third time is a charm %s."]
    if seen < len(templates):
        greeting = templates[seen] % name
    else:
        greeting = "Nice to see you at the %d-nth time %s!" % (seen, name)

    if seen > 1 and last_seen:
        greeting = "%s %f seconds had passed since the last time we saw you!" % (greeting, time.time() - last_seen.timestamp)

    response = GreetResponse()
    response.name = name
    response.greeting = greeting

    return response


handler = RequestReplyHandler(functions)

#
# Serve the endpoint
#

from flask import request
from flask import make_response
from flask import Flask

app = Flask(__name__)


@app.route('/service', methods=['POST'])
def handle():
    response_data = handler(request.data)
    response = make_response(response_data)
    response.headers.set('Content-Type', 'application/octet-stream')
    return response


if __name__ == "__main__":
    app.run()

