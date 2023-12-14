# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend_pb2 as backend__pb2


class SDMS_BackendStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStudentDetails = channel.unary_unary(
                '/SDMS_Backend/GetStudentDetails',
                request_serializer=backend__pb2.IDRequest.SerializeToString,
                response_deserializer=backend__pb2.StudentDetailsReply.FromString,
                )


class SDMS_BackendServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStudentDetails(self, request, context):
        """rpc SayHello (HelloRequest) returns (HelloReply) {}
        rpc Login (LoginRequest) returns (LoginReply) {}
        rpc GetGrade (GradeRequest) returns (GradeReply) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SDMS_BackendServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStudentDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudentDetails,
                    request_deserializer=backend__pb2.IDRequest.FromString,
                    response_serializer=backend__pb2.StudentDetailsReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SDMS_Backend', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SDMS_Backend(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStudentDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SDMS_Backend/GetStudentDetails',
            backend__pb2.IDRequest.SerializeToString,
            backend__pb2.StudentDetailsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)