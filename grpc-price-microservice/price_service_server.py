import price_service_logic as logic
from proto import price_service_pb2
from proto import price_service_pb2_grpc
import custom_objects
import custom_exception
import grpc
from concurrent import futures

class PriceServicer():

    def ReadItemInfo(self, request, context):
        res = logic.get_item_info_list(request.item_id)
        list = [price_service_pb2.ItemDetail(item_id=x['item_id'], item_name=x['item_name'], shop_id=x['shop_id']) for x in res]
        return price_service_pb2.ReadItemInfoResponse(item_details=list)

    def ReadItemDetails(self, request, context):
        res = logic.get_item_detail(request.item_id)

        if res is None:
            item = price_service_pb2.ItemDetail(item_id=-1,item_name=None,shop_id=-1,)
            return  price_service_pb2.ReadItemDetailResponse(itemDetail=item, notFound=1)
        
        item = price_service_pb2.ItemDetail(item_id=res['item_id'], item_name=res['item_name'], shop_id=res['shop_id'])
        return price_service_pb2.ReadItemDetailResponse(itemDetail=item, notFound=-1)


    def CreateItemDetailPrice(self, request, context):
        try:
            logic.add_item(request.item_id, request.shop_id)
        except custom_exception.NotFoundError as err:
            print(err)
            return price_service_pb2.CreateItemDetailPriceResponse(success=-1)
            
        
        return price_service_pb2.CreateItemDetailPriceResponse(success=1)


    def ReadPriceChange(self, request, context):
        res = logic.get_item_price_change(request.item_id)
        list = []
        if len(res) == 0:
            list.append(price_service_pb2.PriceLogItem(price=-1, time=-1))
            return price_service_pb2.ReadPriceChangeResponse(list=list, notFound=1)
        list = [price_service_pb2.PriceLogItem(price=x['price'], time=logic.timestamp_from_datetime(x['time'])) for x in res]
        return price_service_pb2.ReadPriceChangeResponse(list=list, notFound=-1)

def serve():
    port = '[::]:8080'
    print('Starting price tracker server...')
    print('Listening on port ' + port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    price_service_pb2_grpc.add_PriceServiceServicer_to_server(
        PriceServicer(), server)
    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()

serve()
