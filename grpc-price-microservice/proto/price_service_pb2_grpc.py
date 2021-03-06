# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import price_service_pb2 as price__service__pb2


class PriceServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadItemDetails = channel.unary_unary(
                '/priceServicePackage.PriceService/ReadItemDetails',
                request_serializer=price__service__pb2.ReadItemDetailRequest.SerializeToString,
                response_deserializer=price__service__pb2.ReadItemDetailResponse.FromString,
                )
        self.CreateItemDetailPrice = channel.unary_unary(
                '/priceServicePackage.PriceService/CreateItemDetailPrice',
                request_serializer=price__service__pb2.CreateItemDetailPriceRequest.SerializeToString,
                response_deserializer=price__service__pb2.CreateItemDetailPriceResponse.FromString,
                )
        self.ReadPriceChange = channel.unary_unary(
                '/priceServicePackage.PriceService/ReadPriceChange',
                request_serializer=price__service__pb2.ReadPriceChangeRequest.SerializeToString,
                response_deserializer=price__service__pb2.ReadPriceChangeResponse.FromString,
                )
        self.ReadItemInfo = channel.unary_unary(
                '/priceServicePackage.PriceService/ReadItemInfo',
                request_serializer=price__service__pb2.ReadItemInfoRequest.SerializeToString,
                response_deserializer=price__service__pb2.ReadItemInfoResponse.FromString,
                )


class PriceServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def ReadItemDetails(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateItemDetailPrice(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadPriceChange(self, request, context):
        """rpc ReadFlashSales(ReadFlashSalesRequest) returns (ReadFlashSalesResponse);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadItemInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PriceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadItemDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadItemDetails,
                    request_deserializer=price__service__pb2.ReadItemDetailRequest.FromString,
                    response_serializer=price__service__pb2.ReadItemDetailResponse.SerializeToString,
            ),
            'CreateItemDetailPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateItemDetailPrice,
                    request_deserializer=price__service__pb2.CreateItemDetailPriceRequest.FromString,
                    response_serializer=price__service__pb2.CreateItemDetailPriceResponse.SerializeToString,
            ),
            'ReadPriceChange': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadPriceChange,
                    request_deserializer=price__service__pb2.ReadPriceChangeRequest.FromString,
                    response_serializer=price__service__pb2.ReadPriceChangeResponse.SerializeToString,
            ),
            'ReadItemInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadItemInfo,
                    request_deserializer=price__service__pb2.ReadItemInfoRequest.FromString,
                    response_serializer=price__service__pb2.ReadItemInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'priceServicePackage.PriceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PriceService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def ReadItemDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/priceServicePackage.PriceService/ReadItemDetails',
            price__service__pb2.ReadItemDetailRequest.SerializeToString,
            price__service__pb2.ReadItemDetailResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateItemDetailPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/priceServicePackage.PriceService/CreateItemDetailPrice',
            price__service__pb2.CreateItemDetailPriceRequest.SerializeToString,
            price__service__pb2.CreateItemDetailPriceResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadPriceChange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/priceServicePackage.PriceService/ReadPriceChange',
            price__service__pb2.ReadPriceChangeRequest.SerializeToString,
            price__service__pb2.ReadPriceChangeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadItemInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/priceServicePackage.PriceService/ReadItemInfo',
            price__service__pb2.ReadItemInfoRequest.SerializeToString,
            price__service__pb2.ReadItemInfoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
