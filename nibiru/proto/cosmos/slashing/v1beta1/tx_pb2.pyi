"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MsgUnjail(google.protobuf.message.Message):
    """MsgUnjail defines the Msg/Unjail request type"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALIDATOR_ADDR_FIELD_NUMBER: builtins.int
    validator_addr: typing.Text
    def __init__(self,
        *,
        validator_addr: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["validator_addr",b"validator_addr"]) -> None: ...
global___MsgUnjail = MsgUnjail

class MsgUnjailResponse(google.protobuf.message.Message):
    """MsgUnjailResponse defines the Msg/Unjail response type"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___MsgUnjailResponse = MsgUnjailResponse
