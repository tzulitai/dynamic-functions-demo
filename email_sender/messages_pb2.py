# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0emessages.proto\x12\x07\x65xample\"\x1c\n\x0cGreetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"G\n\rGreetResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\x12\x16\n\x0e\x65lapsed_millis\x18\x03 \x01(\x03\"\x19\n\tSeenCount\x12\x0c\n\x04seen\x18\x01 \x01(\x03\",\n\x17LastSeenTimestampMillis\x12\x11\n\ttimestamp\x18\x01 \x01(\x02\"\x1a\n\x05\x45mail\x12\x11\n\trecipient\x18\x01 \x01(\tb\x06proto3'
)




_GREETREQUEST = _descriptor.Descriptor(
  name='GreetRequest',
  full_name='example.GreetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.GreetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=55,
)


_GREETRESPONSE = _descriptor.Descriptor(
  name='GreetResponse',
  full_name='example.GreetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.GreetResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='greeting', full_name='example.GreetResponse.greeting', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed_millis', full_name='example.GreetResponse.elapsed_millis', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=128,
)


_SEENCOUNT = _descriptor.Descriptor(
  name='SeenCount',
  full_name='example.SeenCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seen', full_name='example.SeenCount.seen', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=155,
)


_LASTSEENTIMESTAMPMILLIS = _descriptor.Descriptor(
  name='LastSeenTimestampMillis',
  full_name='example.LastSeenTimestampMillis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='example.LastSeenTimestampMillis.timestamp', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=201,
)


_EMAIL = _descriptor.Descriptor(
  name='Email',
  full_name='example.Email',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipient', full_name='example.Email.recipient', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['GreetRequest'] = _GREETREQUEST
DESCRIPTOR.message_types_by_name['GreetResponse'] = _GREETRESPONSE
DESCRIPTOR.message_types_by_name['SeenCount'] = _SEENCOUNT
DESCRIPTOR.message_types_by_name['LastSeenTimestampMillis'] = _LASTSEENTIMESTAMPMILLIS
DESCRIPTOR.message_types_by_name['Email'] = _EMAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GreetRequest = _reflection.GeneratedProtocolMessageType('GreetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GREETREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:example.GreetRequest)
  })
_sym_db.RegisterMessage(GreetRequest)

GreetResponse = _reflection.GeneratedProtocolMessageType('GreetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GREETRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:example.GreetResponse)
  })
_sym_db.RegisterMessage(GreetResponse)

SeenCount = _reflection.GeneratedProtocolMessageType('SeenCount', (_message.Message,), {
  'DESCRIPTOR' : _SEENCOUNT,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:example.SeenCount)
  })
_sym_db.RegisterMessage(SeenCount)

LastSeenTimestampMillis = _reflection.GeneratedProtocolMessageType('LastSeenTimestampMillis', (_message.Message,), {
  'DESCRIPTOR' : _LASTSEENTIMESTAMPMILLIS,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:example.LastSeenTimestampMillis)
  })
_sym_db.RegisterMessage(LastSeenTimestampMillis)

Email = _reflection.GeneratedProtocolMessageType('Email', (_message.Message,), {
  'DESCRIPTOR' : _EMAIL,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:example.Email)
  })
_sym_db.RegisterMessage(Email)


# @@protoc_insertion_point(module_scope)
