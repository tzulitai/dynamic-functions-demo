from messages_pb2 import Email

from statefun import StatefulFunctions
from statefun import StateSpec
from statefun import RequestReplyHandler
from statefun import kafka_egress_record

functions = StatefulFunctions()


@functions.bind(typename="com.foo.bar/email_sender")
def send_email(context, email: Email):
    egress_message = kafka_egress_record(topic="emails", value=email)
    context.pack_and_send_egress("com.foo.bar/greets", egress_message)


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

