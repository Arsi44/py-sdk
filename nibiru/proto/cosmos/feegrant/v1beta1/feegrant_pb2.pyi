"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BasicAllowance(google.protobuf.message.Message):
    """BasicAllowance implements Allowance with a one-time grant of tokens
    that optionally expires. The grantee can use up to SpendLimit to cover fees.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SPEND_LIMIT_FIELD_NUMBER: builtins.int
    EXPIRATION_FIELD_NUMBER: builtins.int
    @property
    def spend_limit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """spend_limit specifies the maximum amount of tokens that can be spent
        by this allowance and will be updated as tokens are spent. If it is
        empty, there is no spend limit and any amount of coins can be spent.
        """
        pass
    @property
    def expiration(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """expiration specifies an optional time when this allowance expires"""
        pass
    def __init__(self,
        *,
        spend_limit: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        expiration: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expiration",b"expiration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expiration",b"expiration","spend_limit",b"spend_limit"]) -> None: ...
global___BasicAllowance = BasicAllowance

class PeriodicAllowance(google.protobuf.message.Message):
    """PeriodicAllowance extends Allowance to allow for both a maximum cap,
    as well as a limit per time period.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASIC_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    PERIOD_SPEND_LIMIT_FIELD_NUMBER: builtins.int
    PERIOD_CAN_SPEND_FIELD_NUMBER: builtins.int
    PERIOD_RESET_FIELD_NUMBER: builtins.int
    @property
    def basic(self) -> global___BasicAllowance:
        """basic specifies a struct of `BasicAllowance`"""
        pass
    @property
    def period(self) -> google.protobuf.duration_pb2.Duration:
        """period specifies the time duration in which period_spend_limit coins can
        be spent before that allowance is reset
        """
        pass
    @property
    def period_spend_limit(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """period_spend_limit specifies the maximum number of coins that can be spent
        in the period
        """
        pass
    @property
    def period_can_spend(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """period_can_spend is the number of coins left to be spent before the period_reset time"""
        pass
    @property
    def period_reset(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """period_reset is the time at which this period resets and a new one begins,
        it is calculated from the start time of the first transaction after the
        last period ended
        """
        pass
    def __init__(self,
        *,
        basic: typing.Optional[global___BasicAllowance] = ...,
        period: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        period_spend_limit: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        period_can_spend: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        period_reset: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["basic",b"basic","period",b"period","period_reset",b"period_reset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["basic",b"basic","period",b"period","period_can_spend",b"period_can_spend","period_reset",b"period_reset","period_spend_limit",b"period_spend_limit"]) -> None: ...
global___PeriodicAllowance = PeriodicAllowance

class AllowedMsgAllowance(google.protobuf.message.Message):
    """AllowedMsgAllowance creates allowance only for specified message types."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALLOWANCE_FIELD_NUMBER: builtins.int
    ALLOWED_MESSAGES_FIELD_NUMBER: builtins.int
    @property
    def allowance(self) -> google.protobuf.any_pb2.Any:
        """allowance can be any of basic and filtered fee allowance."""
        pass
    @property
    def allowed_messages(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """allowed_messages are the messages for which the grantee has the access."""
        pass
    def __init__(self,
        *,
        allowance: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        allowed_messages: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allowance",b"allowance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowance",b"allowance","allowed_messages",b"allowed_messages"]) -> None: ...
global___AllowedMsgAllowance = AllowedMsgAllowance

class Grant(google.protobuf.message.Message):
    """Grant is stored in the KVStore to record a grant with full context"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    ALLOWANCE_FIELD_NUMBER: builtins.int
    granter: typing.Text
    """granter is the address of the user granting an allowance of their funds."""

    grantee: typing.Text
    """grantee is the address of the user being granted an allowance of another user's funds."""

    @property
    def allowance(self) -> google.protobuf.any_pb2.Any:
        """allowance can be any of basic and filtered fee allowance."""
        pass
    def __init__(self,
        *,
        granter: typing.Text = ...,
        grantee: typing.Text = ...,
        allowance: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allowance",b"allowance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowance",b"allowance","grantee",b"grantee","granter",b"granter"]) -> None: ...
global___Grant = Grant
