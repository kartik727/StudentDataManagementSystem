# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbackend.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"C\n\x0cGradeRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ourse_code\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"\x1b\n\nGradeReply\x12\r\n\x05grade\x18\x01 \x01(\t\"?\n\x0cLoginRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\"\x1b\n\nLoginReply\x12\r\n\x05token\x18\x01 \x01(\t\"+\n\tIDRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"\x84\x01\n\x13StudentDetailsReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x12\n\ndepartment\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65gree\x18\x04 \x01(\t\x12\x17\n\x0fgraduation_year\x18\x05 \x01(\t\x12\x13\n\x0b\x63urrent_gpa\x18\x06 \x01(\t2\x89\x01\n\x0cSDMS_Backend\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x12%\n\x05Login\x12\r.LoginRequest\x1a\x0b.LoginReply\"\x00\x12(\n\x08GetGrade\x12\r.GradeRequest\x1a\x0b.GradeReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backend_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=17
  _globals['_HELLOREQUEST']._serialized_end=45
  _globals['_HELLOREPLY']._serialized_start=47
  _globals['_HELLOREPLY']._serialized_end=76
  _globals['_GRADEREQUEST']._serialized_start=78
  _globals['_GRADEREQUEST']._serialized_end=145
  _globals['_GRADEREPLY']._serialized_start=147
  _globals['_GRADEREPLY']._serialized_end=174
  _globals['_LOGINREQUEST']._serialized_start=176
  _globals['_LOGINREQUEST']._serialized_end=239
  _globals['_LOGINREPLY']._serialized_start=241
  _globals['_LOGINREPLY']._serialized_end=268
  _globals['_IDREQUEST']._serialized_start=270
  _globals['_IDREQUEST']._serialized_end=313
  _globals['_STUDENTDETAILSREPLY']._serialized_start=316
  _globals['_STUDENTDETAILSREPLY']._serialized_end=448
  _globals['_SDMS_BACKEND']._serialized_start=451
  _globals['_SDMS_BACKEND']._serialized_end=588
# @@protoc_insertion_point(module_scope)
