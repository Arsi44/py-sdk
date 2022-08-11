"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common.common_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Params(google.protobuf.message.Message):
    """Params defines the parameters for the x/pricefeed module."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIRS_FIELD_NUMBER: builtins.int
    TWAP_LOOKBACK_WINDOW_FIELD_NUMBER: builtins.int
    @property
    def pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common.common_pb2.AssetPair]:
        """Pairs is the list of valid trading pairs for the module.
        Add new trading pairs
        """
        pass
    @property
    def twap_lookback_window(self) -> google.protobuf.duration_pb2.Duration:
        """amount of time to look back for TWAP calculations"""
        pass
    def __init__(self,
        *,
        pairs: typing.Optional[typing.Iterable[common.common_pb2.AssetPair]] = ...,
        twap_lookback_window: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["twap_lookback_window",b"twap_lookback_window"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pairs",b"pairs","twap_lookback_window",b"twap_lookback_window"]) -> None: ...
global___Params = Params

class OraclesMarshaler(google.protobuf.message.Message):
    """OraclesMarshaler is a codec.ProtoMarshaler for an oracles array in the
    OraclesState sdk.KVStore.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ORACLES_FIELD_NUMBER: builtins.int
    @property
    def oracles(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self,
        *,
        oracles: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["oracles",b"oracles"]) -> None: ...
global___OraclesMarshaler = OraclesMarshaler

class ActivePairMarshaler(google.protobuf.message.Message):
    """ActivePairMarshaler is a codec.ProtoMarshaler for the "IsActive" status of
    a pair in the ActivePairState sdk.KVStore.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    is_active: builtins.bool
    def __init__(self,
        *,
        is_active: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["is_active",b"is_active"]) -> None: ...
global___ActivePairMarshaler = ActivePairMarshaler

class PostedPrice(google.protobuf.message.Message):
    """PostedPrice defines a price for an asset pair posted by a specific oracle."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_ID_FIELD_NUMBER: builtins.int
    ORACLE_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    EXPIRY_FIELD_NUMBER: builtins.int
    pair_id: typing.Text
    oracle: typing.Text
    price: typing.Text
    @property
    def expiry(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        pair_id: typing.Text = ...,
        oracle: typing.Text = ...,
        price: typing.Text = ...,
        expiry: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expiry",b"expiry"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expiry",b"expiry","oracle",b"oracle","pair_id",b"pair_id","price",b"price"]) -> None: ...
global___PostedPrice = PostedPrice

class CurrentPrice(google.protobuf.message.Message):
    """CurrentPrice defines the current price for an asset pair in the pricefeed
    module.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_ID_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    pair_id: typing.Text
    price: typing.Text
    def __init__(self,
        *,
        pair_id: typing.Text = ...,
        price: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pair_id",b"pair_id","price",b"price"]) -> None: ...
global___CurrentPrice = CurrentPrice

class CurrentTWAP(google.protobuf.message.Message):
    """CurrentTWAP states defines the numerator and denominator for the TWAP calculation"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAIR_ID_FIELD_NUMBER: builtins.int
    NUMERATOR_FIELD_NUMBER: builtins.int
    DENOMINATOR_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    pair_id: typing.Text
    numerator: typing.Text
    denominator: typing.Text
    price: typing.Text
    def __init__(self,
        *,
        pair_id: typing.Text = ...,
        numerator: typing.Text = ...,
        denominator: typing.Text = ...,
        price: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denominator",b"denominator","numerator",b"numerator","pair_id",b"pair_id","price",b"price"]) -> None: ...
global___CurrentTWAP = CurrentTWAP
