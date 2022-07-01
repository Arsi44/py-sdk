"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import perp.v1.query_pb2

class QueryStub:
    """Query defines the gRPC querier service."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Params: grpc.UnaryUnaryMultiCallable[
        perp.v1.query_pb2.QueryParamsRequest,
        perp.v1.query_pb2.QueryParamsResponse]
    """Parameters queries the parameters of the x/perp module."""

    TraderPosition: grpc.UnaryUnaryMultiCallable[
        perp.v1.query_pb2.QueryTraderPositionRequest,
        perp.v1.query_pb2.QueryTraderPositionResponse]


class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""
    @abc.abstractmethod
    def Params(self,
        request: perp.v1.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> perp.v1.query_pb2.QueryParamsResponse:
        """Parameters queries the parameters of the x/perp module."""
        pass

    @abc.abstractmethod
    def TraderPosition(self,
        request: perp.v1.query_pb2.QueryTraderPositionRequest,
        context: grpc.ServicerContext,
    ) -> perp.v1.query_pb2.QueryTraderPositionResponse: ...


def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
