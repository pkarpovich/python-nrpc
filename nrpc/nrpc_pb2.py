# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: nrpc/nrpc.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'nrpc/nrpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fnrpc/nrpc.proto\x12\x04nrpc\x1a google/protobuf/descriptor.proto\"\x86\x01\n\x05\x45rror\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.nrpc.Error.Type\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x10\n\x08msgCount\x18\x03 \x01(\r\":\n\x04Type\x12\n\n\x06\x43LIENT\x10\x00\x12\n\n\x06SERVER\x10\x01\x12\x07\n\x03\x45OS\x10\x03\x12\x11\n\rSERVERTOOBUSY\x10\x04\"\x06\n\x04Void\"\x0b\n\tNoRequest\"\t\n\x07NoReply\"\x1d\n\tHeartBeat\x12\x10\n\x08lastbeat\x18\x01 \x01(\x08*$\n\x0bSubjectRule\x12\x08\n\x04\x43OPY\x10\x00\x12\x0b\n\x07TOLOWER\x10\x01:6\n\x0epackageSubject\x12\x1c.google.protobuf.FileOptions\x18\xd0\x86\x03 \x01(\t:<\n\x14packageSubjectParams\x12\x1c.google.protobuf.FileOptions\x18\xd1\x86\x03 \x03(\t:M\n\x12serviceSubjectRule\x12\x1c.google.protobuf.FileOptions\x18\xd2\x86\x03 \x01(\x0e\x32\x11.nrpc.SubjectRule:L\n\x11methodSubjectRule\x12\x1c.google.protobuf.FileOptions\x18\xd3\x86\x03 \x01(\x0e\x32\x11.nrpc.SubjectRule:9\n\x0eserviceSubject\x12\x1f.google.protobuf.ServiceOptions\x18\xb8\x8e\x03 \x01(\t:?\n\x14serviceSubjectParams\x12\x1f.google.protobuf.ServiceOptions\x18\xb9\x8e\x03 \x03(\t:7\n\rmethodSubject\x12\x1e.google.protobuf.MethodOptions\x18\xa0\x96\x03 \x01(\t:=\n\x13methodSubjectParams\x12\x1e.google.protobuf.MethodOptions\x18\xa1\x96\x03 \x03(\t:7\n\rstreamedReply\x12\x1e.google.protobuf.MethodOptions\x18\xa2\x96\x03 \x01(\x08\x42\x1aZ\x18github.com/nats-rpc/nrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nrpc.nrpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\030github.com/nats-rpc/nrpc'
  _globals['_SUBJECTRULE']._serialized_start=259
  _globals['_SUBJECTRULE']._serialized_end=295
  _globals['_ERROR']._serialized_start=60
  _globals['_ERROR']._serialized_end=194
  _globals['_ERROR_TYPE']._serialized_start=136
  _globals['_ERROR_TYPE']._serialized_end=194
  _globals['_VOID']._serialized_start=196
  _globals['_VOID']._serialized_end=202
  _globals['_NOREQUEST']._serialized_start=204
  _globals['_NOREQUEST']._serialized_end=215
  _globals['_NOREPLY']._serialized_start=217
  _globals['_NOREPLY']._serialized_end=226
  _globals['_HEARTBEAT']._serialized_start=228
  _globals['_HEARTBEAT']._serialized_end=257
# @@protoc_insertion_point(module_scope)
