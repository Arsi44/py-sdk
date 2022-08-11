# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/multisig/v1beta1/multisig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-cosmos/crypto/multisig/v1beta1/multisig.proto\x12\x1e\x63osmos.crypto.multisig.v1beta1\x1a\x14gogoproto/gogo.proto\"*\n\x0eMultiSignature\x12\x12\n\nsignatures\x18\x01 \x03(\x0c:\x04\xd0\xa1\x1f\x01\"A\n\x0f\x43ompactBitArray\x12\x19\n\x11\x65xtra_bits_stored\x18\x01 \x01(\r\x12\r\n\x05\x65lems\x18\x02 \x01(\x0c:\x04\x98\xa0\x1f\x00\x42+Z)github.com/cosmos/cosmos-sdk/crypto/typesb\x06proto3'
)


_MULTISIGNATURE = DESCRIPTOR.message_types_by_name['MultiSignature']
_COMPACTBITARRAY = DESCRIPTOR.message_types_by_name['CompactBitArray']
MultiSignature = _reflection.GeneratedProtocolMessageType(
    'MultiSignature',
    (_message.Message,),
    {
        'DESCRIPTOR': _MULTISIGNATURE,
        '__module__': 'cosmos.crypto.multisig.v1beta1.multisig_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.crypto.multisig.v1beta1.MultiSignature)
    },
)
_sym_db.RegisterMessage(MultiSignature)

CompactBitArray = _reflection.GeneratedProtocolMessageType(
    'CompactBitArray',
    (_message.Message,),
    {
        'DESCRIPTOR': _COMPACTBITARRAY,
        '__module__': 'cosmos.crypto.multisig.v1beta1.multisig_pb2'
        # @@protoc_insertion_point(class_scope:cosmos.crypto.multisig.v1beta1.CompactBitArray)
    },
)
_sym_db.RegisterMessage(CompactBitArray)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/crypto/types'
    _MULTISIGNATURE._options = None
    _MULTISIGNATURE._serialized_options = b'\320\241\037\001'
    _COMPACTBITARRAY._options = None
    _COMPACTBITARRAY._serialized_options = b'\230\240\037\000'
    _MULTISIGNATURE._serialized_start = 103
    _MULTISIGNATURE._serialized_end = 145
    _COMPACTBITARRAY._serialized_start = 147
    _COMPACTBITARRAY._serialized_end = 212
# @@protoc_insertion_point(module_scope)
