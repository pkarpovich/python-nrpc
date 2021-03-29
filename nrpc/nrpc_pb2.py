# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nrpc/nrpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="nrpc/nrpc.proto",
    package="nrpc",
    syntax="proto3",
    serialized_options=b"Z\030github.com/nats-rpc/nrpc",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0fnrpc/nrpc.proto\x12\x04nrpc\x1a google/protobuf/descriptor.proto"\x86\x01\n\x05\x45rror\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.nrpc.Error.Type\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x10\n\x08msgCount\x18\x03 \x01(\r":\n\x04Type\x12\n\n\x06\x43LIENT\x10\x00\x12\n\n\x06SERVER\x10\x01\x12\x07\n\x03\x45OS\x10\x03\x12\x11\n\rSERVERTOOBUSY\x10\x04"\x06\n\x04Void"\x0b\n\tNoRequest"\t\n\x07NoReply"\x1d\n\tHeartBeat\x12\x10\n\x08lastbeat\x18\x01 \x01(\x08*$\n\x0bSubjectRule\x12\x08\n\x04\x43OPY\x10\x00\x12\x0b\n\x07TOLOWER\x10\x01:6\n\x0epackageSubject\x12\x1c.google.protobuf.FileOptions\x18\xd0\x86\x03 \x01(\t:<\n\x14packageSubjectParams\x12\x1c.google.protobuf.FileOptions\x18\xd1\x86\x03 \x03(\t:M\n\x12serviceSubjectRule\x12\x1c.google.protobuf.FileOptions\x18\xd2\x86\x03 \x01(\x0e\x32\x11.nrpc.SubjectRule:L\n\x11methodSubjectRule\x12\x1c.google.protobuf.FileOptions\x18\xd3\x86\x03 \x01(\x0e\x32\x11.nrpc.SubjectRule:9\n\x0eserviceSubject\x12\x1f.google.protobuf.ServiceOptions\x18\xb8\x8e\x03 \x01(\t:?\n\x14serviceSubjectParams\x12\x1f.google.protobuf.ServiceOptions\x18\xb9\x8e\x03 \x03(\t:7\n\rmethodSubject\x12\x1e.google.protobuf.MethodOptions\x18\xa0\x96\x03 \x01(\t:=\n\x13methodSubjectParams\x12\x1e.google.protobuf.MethodOptions\x18\xa1\x96\x03 \x03(\t:7\n\rstreamedReply\x12\x1e.google.protobuf.MethodOptions\x18\xa2\x96\x03 \x01(\x08\x42\x1aZ\x18github.com/nats-rpc/nrpcb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,
    ],
)

_SUBJECTRULE = _descriptor.EnumDescriptor(
    name="SubjectRule",
    full_name="nrpc.SubjectRule",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="COPY",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TOLOWER",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=259,
    serialized_end=295,
)
_sym_db.RegisterEnumDescriptor(_SUBJECTRULE)

SubjectRule = enum_type_wrapper.EnumTypeWrapper(_SUBJECTRULE)
COPY = 0
TOLOWER = 1

PACKAGESUBJECT_FIELD_NUMBER = 50000
packageSubject = _descriptor.FieldDescriptor(
    name="packageSubject",
    full_name="nrpc.packageSubject",
    index=0,
    number=50000,
    type=9,
    cpp_type=9,
    label=1,
    has_default_value=False,
    default_value=b"".decode("utf-8"),
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
PACKAGESUBJECTPARAMS_FIELD_NUMBER = 50001
packageSubjectParams = _descriptor.FieldDescriptor(
    name="packageSubjectParams",
    full_name="nrpc.packageSubjectParams",
    index=1,
    number=50001,
    type=9,
    cpp_type=9,
    label=3,
    has_default_value=False,
    default_value=[],
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
SERVICESUBJECTRULE_FIELD_NUMBER = 50002
serviceSubjectRule = _descriptor.FieldDescriptor(
    name="serviceSubjectRule",
    full_name="nrpc.serviceSubjectRule",
    index=2,
    number=50002,
    type=14,
    cpp_type=8,
    label=1,
    has_default_value=False,
    default_value=0,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
METHODSUBJECTRULE_FIELD_NUMBER = 50003
methodSubjectRule = _descriptor.FieldDescriptor(
    name="methodSubjectRule",
    full_name="nrpc.methodSubjectRule",
    index=3,
    number=50003,
    type=14,
    cpp_type=8,
    label=1,
    has_default_value=False,
    default_value=0,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
SERVICESUBJECT_FIELD_NUMBER = 51000
serviceSubject = _descriptor.FieldDescriptor(
    name="serviceSubject",
    full_name="nrpc.serviceSubject",
    index=4,
    number=51000,
    type=9,
    cpp_type=9,
    label=1,
    has_default_value=False,
    default_value=b"".decode("utf-8"),
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
SERVICESUBJECTPARAMS_FIELD_NUMBER = 51001
serviceSubjectParams = _descriptor.FieldDescriptor(
    name="serviceSubjectParams",
    full_name="nrpc.serviceSubjectParams",
    index=5,
    number=51001,
    type=9,
    cpp_type=9,
    label=3,
    has_default_value=False,
    default_value=[],
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
METHODSUBJECT_FIELD_NUMBER = 52000
methodSubject = _descriptor.FieldDescriptor(
    name="methodSubject",
    full_name="nrpc.methodSubject",
    index=6,
    number=52000,
    type=9,
    cpp_type=9,
    label=1,
    has_default_value=False,
    default_value=b"".decode("utf-8"),
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
METHODSUBJECTPARAMS_FIELD_NUMBER = 52001
methodSubjectParams = _descriptor.FieldDescriptor(
    name="methodSubjectParams",
    full_name="nrpc.methodSubjectParams",
    index=7,
    number=52001,
    type=9,
    cpp_type=9,
    label=3,
    has_default_value=False,
    default_value=[],
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
STREAMEDREPLY_FIELD_NUMBER = 52002
streamedReply = _descriptor.FieldDescriptor(
    name="streamedReply",
    full_name="nrpc.streamedReply",
    index=8,
    number=52002,
    type=8,
    cpp_type=7,
    label=1,
    has_default_value=False,
    default_value=False,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)

_ERROR_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="nrpc.Error.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CLIENT",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVER",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EOS",
            index=2,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVERTOOBUSY",
            index=3,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=136,
    serialized_end=194,
)
_sym_db.RegisterEnumDescriptor(_ERROR_TYPE)


_ERROR = _descriptor.Descriptor(
    name="Error",
    full_name="nrpc.Error",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="nrpc.Error.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="message",
            full_name="nrpc.Error.message",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="msgCount",
            full_name="nrpc.Error.msgCount",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _ERROR_TYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=60,
    serialized_end=194,
)


_VOID = _descriptor.Descriptor(
    name="Void",
    full_name="nrpc.Void",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=196,
    serialized_end=202,
)


_NOREQUEST = _descriptor.Descriptor(
    name="NoRequest",
    full_name="nrpc.NoRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=204,
    serialized_end=215,
)


_NOREPLY = _descriptor.Descriptor(
    name="NoReply",
    full_name="nrpc.NoReply",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=217,
    serialized_end=226,
)


_HEARTBEAT = _descriptor.Descriptor(
    name="HeartBeat",
    full_name="nrpc.HeartBeat",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="lastbeat",
            full_name="nrpc.HeartBeat.lastbeat",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=228,
    serialized_end=257,
)

_ERROR.fields_by_name["type"].enum_type = _ERROR_TYPE
_ERROR_TYPE.containing_type = _ERROR
DESCRIPTOR.message_types_by_name["Error"] = _ERROR
DESCRIPTOR.message_types_by_name["Void"] = _VOID
DESCRIPTOR.message_types_by_name["NoRequest"] = _NOREQUEST
DESCRIPTOR.message_types_by_name["NoReply"] = _NOREPLY
DESCRIPTOR.message_types_by_name["HeartBeat"] = _HEARTBEAT
DESCRIPTOR.enum_types_by_name["SubjectRule"] = _SUBJECTRULE
DESCRIPTOR.extensions_by_name["packageSubject"] = packageSubject
DESCRIPTOR.extensions_by_name["packageSubjectParams"] = packageSubjectParams
DESCRIPTOR.extensions_by_name["serviceSubjectRule"] = serviceSubjectRule
DESCRIPTOR.extensions_by_name["methodSubjectRule"] = methodSubjectRule
DESCRIPTOR.extensions_by_name["serviceSubject"] = serviceSubject
DESCRIPTOR.extensions_by_name["serviceSubjectParams"] = serviceSubjectParams
DESCRIPTOR.extensions_by_name["methodSubject"] = methodSubject
DESCRIPTOR.extensions_by_name["methodSubjectParams"] = methodSubjectParams
DESCRIPTOR.extensions_by_name["streamedReply"] = streamedReply
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Error = _reflection.GeneratedProtocolMessageType(
    "Error",
    (_message.Message,),
    {
        "DESCRIPTOR": _ERROR,
        "__module__": "nrpc.nrpc_pb2"
        # @@protoc_insertion_point(class_scope:nrpc.Error)
    },
)
_sym_db.RegisterMessage(Error)

Void = _reflection.GeneratedProtocolMessageType(
    "Void",
    (_message.Message,),
    {
        "DESCRIPTOR": _VOID,
        "__module__": "nrpc.nrpc_pb2"
        # @@protoc_insertion_point(class_scope:nrpc.Void)
    },
)
_sym_db.RegisterMessage(Void)

NoRequest = _reflection.GeneratedProtocolMessageType(
    "NoRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _NOREQUEST,
        "__module__": "nrpc.nrpc_pb2"
        # @@protoc_insertion_point(class_scope:nrpc.NoRequest)
    },
)
_sym_db.RegisterMessage(NoRequest)

NoReply = _reflection.GeneratedProtocolMessageType(
    "NoReply",
    (_message.Message,),
    {
        "DESCRIPTOR": _NOREPLY,
        "__module__": "nrpc.nrpc_pb2"
        # @@protoc_insertion_point(class_scope:nrpc.NoReply)
    },
)
_sym_db.RegisterMessage(NoReply)

HeartBeat = _reflection.GeneratedProtocolMessageType(
    "HeartBeat",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEARTBEAT,
        "__module__": "nrpc.nrpc_pb2"
        # @@protoc_insertion_point(class_scope:nrpc.HeartBeat)
    },
)
_sym_db.RegisterMessage(HeartBeat)

google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(packageSubject)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(
    packageSubjectParams
)
serviceSubjectRule.enum_type = _SUBJECTRULE
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(
    serviceSubjectRule
)
methodSubjectRule.enum_type = _SUBJECTRULE
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(methodSubjectRule)
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(serviceSubject)
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
    serviceSubjectParams
)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(methodSubject)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(
    methodSubjectParams
)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(streamedReply)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
