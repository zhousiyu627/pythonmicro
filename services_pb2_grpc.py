# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import services_pb2 as services__pb2


class SentimentAnalysisServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnalyzeSentiment = channel.unary_unary(
                '/SentimentAnalysisService/AnalyzeSentiment',
                request_serializer=services__pb2.TextRequest.SerializeToString,
                response_deserializer=services__pb2.SentimentResponse.FromString,
                )


class SentimentAnalysisServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AnalyzeSentiment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SentimentAnalysisServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AnalyzeSentiment': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyzeSentiment,
                    request_deserializer=services__pb2.TextRequest.FromString,
                    response_serializer=services__pb2.SentimentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SentimentAnalysisService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SentimentAnalysisService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AnalyzeSentiment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SentimentAnalysisService/AnalyzeSentiment',
            services__pb2.TextRequest.SerializeToString,
            services__pb2.SentimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class TextInputServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessText = channel.unary_unary(
                '/TextInputService/ProcessText',
                request_serializer=services__pb2.TextRequest.SerializeToString,
                response_deserializer=services__pb2.SentimentResponse.FromString,
                )


class TextInputServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextInputServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessText': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessText,
                    request_deserializer=services__pb2.TextRequest.FromString,
                    response_serializer=services__pb2.SentimentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TextInputService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextInputService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TextInputService/ProcessText',
            services__pb2.TextRequest.SerializeToString,
            services__pb2.SentimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
