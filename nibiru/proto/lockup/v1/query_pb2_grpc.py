# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from lockup.v1 import query_pb2 as lockup_dot_v1_dot_query__pb2


class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LockedCoins = channel.unary_unary(
            '/nibiru.lockup.v1.Query/LockedCoins',
            request_serializer=lockup_dot_v1_dot_query__pb2.QueryLockedCoinsRequest.SerializeToString,
            response_deserializer=lockup_dot_v1_dot_query__pb2.QueryLockedCoinsResponse.FromString,
        )
        self.Lock = channel.unary_unary(
            '/nibiru.lockup.v1.Query/Lock',
            request_serializer=lockup_dot_v1_dot_query__pb2.QueryLockRequest.SerializeToString,
            response_deserializer=lockup_dot_v1_dot_query__pb2.QueryLockResponse.FromString,
        )
        self.LocksByAddress = channel.unary_unary(
            '/nibiru.lockup.v1.Query/LocksByAddress',
            request_serializer=lockup_dot_v1_dot_query__pb2.QueryLocksByAddress.SerializeToString,
            response_deserializer=lockup_dot_v1_dot_query__pb2.QueryLocksByAddressResponse.FromString,
        )


class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LockedCoins(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LocksByAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'LockedCoins': grpc.unary_unary_rpc_method_handler(
            servicer.LockedCoins,
            request_deserializer=lockup_dot_v1_dot_query__pb2.QueryLockedCoinsRequest.FromString,
            response_serializer=lockup_dot_v1_dot_query__pb2.QueryLockedCoinsResponse.SerializeToString,
        ),
        'Lock': grpc.unary_unary_rpc_method_handler(
            servicer.Lock,
            request_deserializer=lockup_dot_v1_dot_query__pb2.QueryLockRequest.FromString,
            response_serializer=lockup_dot_v1_dot_query__pb2.QueryLockResponse.SerializeToString,
        ),
        'LocksByAddress': grpc.unary_unary_rpc_method_handler(
            servicer.LocksByAddress,
            request_deserializer=lockup_dot_v1_dot_query__pb2.QueryLocksByAddress.FromString,
            response_serializer=lockup_dot_v1_dot_query__pb2.QueryLocksByAddressResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler('nibiru.lockup.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LockedCoins(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/nibiru.lockup.v1.Query/LockedCoins',
            lockup_dot_v1_dot_query__pb2.QueryLockedCoinsRequest.SerializeToString,
            lockup_dot_v1_dot_query__pb2.QueryLockedCoinsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Lock(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/nibiru.lockup.v1.Query/Lock',
            lockup_dot_v1_dot_query__pb2.QueryLockRequest.SerializeToString,
            lockup_dot_v1_dot_query__pb2.QueryLockResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def LocksByAddress(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/nibiru.lockup.v1.Query/LocksByAddress',
            lockup_dot_v1_dot_query__pb2.QueryLocksByAddress.SerializeToString,
            lockup_dot_v1_dot_query__pb2.QueryLocksByAddressResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
