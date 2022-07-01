"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PubKey(google.protobuf.message.Message):
    """PubKey defines a secp256k1 public key
    Key is the compressed form of the pubkey. The first byte depends is a 0x02 byte
    if the y-coordinate is the lexicographically largest of the two associated with
    the x-coordinate. Otherwise the first byte is a 0x03.
    This prefix is followed with the x-coordinate.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    def __init__(self,
        *,
        key: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___PubKey = PubKey

class PrivKey(google.protobuf.message.Message):
    """PrivKey defines a secp256k1 private key."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    def __init__(self,
        *,
        key: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___PrivKey = PrivKey
