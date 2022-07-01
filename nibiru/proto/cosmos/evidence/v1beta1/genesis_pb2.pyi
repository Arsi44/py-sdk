"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the evidence module's genesis state."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    EVIDENCE_FIELD_NUMBER: builtins.int
    @property
    def evidence(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]:
        """evidence defines all the evidence at genesis."""
        pass
    def __init__(self,
        *,
        evidence: typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["evidence",b"evidence"]) -> None: ...
global___GenesisState = GenesisState
