import grpc
from proto import price_service_pb2_grpc, price_service_pb2


def guide_create_item(stub):
    
    createItemDetailPriceRequest = price_service_pb2.CreateItemDetailPriceRequest(item_id=7017331930, shop_id=215845413)
    print(stub.CreateItemDetailPrice(createItemDetailPriceRequest))

    createItemDetailPriceRequest = price_service_pb2.CreateItemDetailPriceRequest(item_id=1313828246, shop_id=10151)
    print(stub.CreateItemDetailPrice(createItemDetailPriceRequest))

def guide_read_item(stub):
    request = price_service_pb2.ReadItemDetailRequest(item_id=7017331930)
    print(stub.ReadItemDetails(request))

    request = price_service_pb2.ReadItemDetailRequest(item_id=1313828246)
    print(stub.ReadItemDetails(request))

    #not found
    request = price_service_pb2.ReadItemDetailRequest(item_id=3307965432)
    print(stub.ReadItemDetails(request))

def guide_read_item_price_change(stub):
    request = price_service_pb2.ReadPriceChangeRequest(item_id=7017331930)
    print(stub.ReadPriceChange(request))

    # not found
    request = price_service_pb2.ReadPriceChangeRequest(item_id=1313828246)
    print(stub.ReadPriceChange(request))

def guide_read_item_info(stub):
    list = [7017331930, 1313828246]
    request = price_service_pb2.ReadItemInfoRequest(item_id=list)
    print(stub.ReadItemInfo(request))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = price_service_pb2_grpc.PriceServiceStub(channel)
        print("-------------- CreateItems --------------")
        guide_create_item(stub)
        print("-------------- ReadPriceChange --------------")
        guide_read_item_price_change(stub)
        print("-------------- ReadItemDetail --------------")
        guide_read_item(stub)
        print("-------------- ReadItemInfo --------------")
        guide_read_item_info(stub)
     

run()
