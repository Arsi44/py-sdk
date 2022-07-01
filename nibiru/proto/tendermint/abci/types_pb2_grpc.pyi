"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import tendermint.abci.types_pb2

class ABCIApplicationStub:
    """----------------------------------------
    Service Definition

    """
    def __init__(self, channel: grpc.Channel) -> None: ...
    Echo: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestEcho,
        tendermint.abci.types_pb2.ResponseEcho]

    Flush: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestFlush,
        tendermint.abci.types_pb2.ResponseFlush]

    Info: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestInfo,
        tendermint.abci.types_pb2.ResponseInfo]

    SetOption: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestSetOption,
        tendermint.abci.types_pb2.ResponseSetOption]

    DeliverTx: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestDeliverTx,
        tendermint.abci.types_pb2.ResponseDeliverTx]

    CheckTx: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestCheckTx,
        tendermint.abci.types_pb2.ResponseCheckTx]

    Query: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestQuery,
        tendermint.abci.types_pb2.ResponseQuery]

    Commit: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestCommit,
        tendermint.abci.types_pb2.ResponseCommit]

    InitChain: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestInitChain,
        tendermint.abci.types_pb2.ResponseInitChain]

    BeginBlock: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestBeginBlock,
        tendermint.abci.types_pb2.ResponseBeginBlock]

    EndBlock: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestEndBlock,
        tendermint.abci.types_pb2.ResponseEndBlock]

    ListSnapshots: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestListSnapshots,
        tendermint.abci.types_pb2.ResponseListSnapshots]

    OfferSnapshot: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestOfferSnapshot,
        tendermint.abci.types_pb2.ResponseOfferSnapshot]

    LoadSnapshotChunk: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestLoadSnapshotChunk,
        tendermint.abci.types_pb2.ResponseLoadSnapshotChunk]

    ApplySnapshotChunk: grpc.UnaryUnaryMultiCallable[
        tendermint.abci.types_pb2.RequestApplySnapshotChunk,
        tendermint.abci.types_pb2.ResponseApplySnapshotChunk]


class ABCIApplicationServicer(metaclass=abc.ABCMeta):
    """----------------------------------------
    Service Definition

    """
    @abc.abstractmethod
    def Echo(self,
        request: tendermint.abci.types_pb2.RequestEcho,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseEcho: ...

    @abc.abstractmethod
    def Flush(self,
        request: tendermint.abci.types_pb2.RequestFlush,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseFlush: ...

    @abc.abstractmethod
    def Info(self,
        request: tendermint.abci.types_pb2.RequestInfo,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseInfo: ...

    @abc.abstractmethod
    def SetOption(self,
        request: tendermint.abci.types_pb2.RequestSetOption,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseSetOption: ...

    @abc.abstractmethod
    def DeliverTx(self,
        request: tendermint.abci.types_pb2.RequestDeliverTx,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseDeliverTx: ...

    @abc.abstractmethod
    def CheckTx(self,
        request: tendermint.abci.types_pb2.RequestCheckTx,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseCheckTx: ...

    @abc.abstractmethod
    def Query(self,
        request: tendermint.abci.types_pb2.RequestQuery,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseQuery: ...

    @abc.abstractmethod
    def Commit(self,
        request: tendermint.abci.types_pb2.RequestCommit,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseCommit: ...

    @abc.abstractmethod
    def InitChain(self,
        request: tendermint.abci.types_pb2.RequestInitChain,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseInitChain: ...

    @abc.abstractmethod
    def BeginBlock(self,
        request: tendermint.abci.types_pb2.RequestBeginBlock,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseBeginBlock: ...

    @abc.abstractmethod
    def EndBlock(self,
        request: tendermint.abci.types_pb2.RequestEndBlock,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseEndBlock: ...

    @abc.abstractmethod
    def ListSnapshots(self,
        request: tendermint.abci.types_pb2.RequestListSnapshots,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseListSnapshots: ...

    @abc.abstractmethod
    def OfferSnapshot(self,
        request: tendermint.abci.types_pb2.RequestOfferSnapshot,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseOfferSnapshot: ...

    @abc.abstractmethod
    def LoadSnapshotChunk(self,
        request: tendermint.abci.types_pb2.RequestLoadSnapshotChunk,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseLoadSnapshotChunk: ...

    @abc.abstractmethod
    def ApplySnapshotChunk(self,
        request: tendermint.abci.types_pb2.RequestApplySnapshotChunk,
        context: grpc.ServicerContext,
    ) -> tendermint.abci.types_pb2.ResponseApplySnapshotChunk: ...


def add_ABCIApplicationServicer_to_server(servicer: ABCIApplicationServicer, server: grpc.Server) -> None: ...
