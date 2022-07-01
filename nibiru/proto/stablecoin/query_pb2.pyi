"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import stablecoin.params_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryParamsRequest(google.protobuf.message.Message):
    """---------------------------------------- Params

    QueryParamsRequest is request type for the Query/Params RPC method.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> stablecoin.params_pb2.Params:
        """params holds all the parameters of this module."""
        pass
    def __init__(self,
        *,
        params: typing.Optional[stablecoin.params_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params",b"params"]) -> None: ...
global___QueryParamsResponse = QueryParamsResponse

class QueryModuleAccountBalances(google.protobuf.message.Message):
    """---------------------------------------- ModuleAccountBalances

    QueryModuleAccountBalances is the request type for the balance of the 
    x/stablecoin module account.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___QueryModuleAccountBalances = QueryModuleAccountBalances

class QueryModuleAccountBalancesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODULEACCOUNTBALANCES_FIELD_NUMBER: builtins.int
    @property
    def moduleAccountBalances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]:
        """ModuleAccountBalances is the balance of all coins in the x/stablecoin module."""
        pass
    def __init__(self,
        *,
        moduleAccountBalances: typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["moduleAccountBalances",b"moduleAccountBalances"]) -> None: ...
global___QueryModuleAccountBalancesResponse = QueryModuleAccountBalancesResponse

class QueryCirculatingSupplies(google.protobuf.message.Message):
    """---------------------------------------- CirculatingSupplies

    QueryCirculatingSupplies is the request type for the circulating supply of
    both NIBI and NUSD.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___QueryCirculatingSupplies = QueryCirculatingSupplies

class QueryCirculatingSuppliesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NIBI_FIELD_NUMBER: builtins.int
    NUSD_FIELD_NUMBER: builtins.int
    @property
    def NIBI(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def NUSD(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(self,
        *,
        NIBI: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        NUSD: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["NIBI",b"NIBI","NUSD",b"NUSD"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["NIBI",b"NIBI","NUSD",b"NUSD"]) -> None: ...
global___QueryCirculatingSuppliesResponse = QueryCirculatingSuppliesResponse

class QueryGovToMintStable(google.protobuf.message.Message):
    """---------------------------------------- GovToMintStable

    QueryGovToMintStable is the request type for the Query/GovToMintStable RPC method
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COLLATERAL_FIELD_NUMBER: builtins.int
    @property
    def collateral(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(self,
        *,
        collateral: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["collateral",b"collateral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["collateral",b"collateral"]) -> None: ...
global___QueryGovToMintStable = QueryGovToMintStable

class QueryGovToMintStableResponse(google.protobuf.message.Message):
    """QueryGovToMintStableResponse is the response type for 'QueryGovToMintStable'"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    GOV_FIELD_NUMBER: builtins.int
    @property
    def gov(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(self,
        *,
        gov: typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gov",b"gov"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gov",b"gov"]) -> None: ...
global___QueryGovToMintStableResponse = QueryGovToMintStableResponse

class LiquidityRatioInfo(google.protobuf.message.Message):
    """---------------------------------------- Liquidity Ratio Info

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LIQUIDITY_RATIO_FIELD_NUMBER: builtins.int
    UPPER_BAND_FIELD_NUMBER: builtins.int
    LOWER_BAND_FIELD_NUMBER: builtins.int
    liquidity_ratio: typing.Text
    upper_band: typing.Text
    lower_band: typing.Text
    def __init__(self,
        *,
        liquidity_ratio: typing.Text = ...,
        upper_band: typing.Text = ...,
        lower_band: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["liquidity_ratio",b"liquidity_ratio","lower_band",b"lower_band","upper_band",b"upper_band"]) -> None: ...
global___LiquidityRatioInfo = LiquidityRatioInfo

class QueryLiquidityRatioInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___QueryLiquidityRatioInfoRequest = QueryLiquidityRatioInfoRequest

class QueryLiquidityRatioInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___LiquidityRatioInfo: ...
    def __init__(self,
        *,
        info: typing.Optional[global___LiquidityRatioInfo] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info",b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info",b"info"]) -> None: ...
global___QueryLiquidityRatioInfoResponse = QueryLiquidityRatioInfoResponse
