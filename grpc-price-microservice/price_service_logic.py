import json
import requests
import time
	
from datetime import datetime

import price_service_storage as storage
import custom_objects
import custom_exception as exception
from proto import price_service_pb2

base_url ='https://shopee.sg/api/v2'

def add_item(item_id, shop_id):
    if storage.item_exist(item_id) is False:
        item_data = get_data_shopee(item_id, shop_id)
        storage.add_item_details(item_data)
        storage.add_item_price(item_data)

def add_item_flash(item):
    if storage.item_exist(item.item_id) is False:
        storage.add_item_details(item)
        storage.add_item_price(item)

def add_item_price(item_id, price, time):
    storage.add_item_price_update(item_id, price, time)
    
def get_item_detail(item_id):
    res = storage.read_item_detail(item_id)
    return res

def get_item_info_list(list):
    res = storage.read_all_items_details(list)
    return res

def get_all_item_ids():
    res = storage.read_all_items()
    return res

def get_item_price_change(item_id):
    res = storage.read_price_change(item_id)
    return res

def get_data_shopee(item_id, shop_id):
    url = base_url + '/item/get'
    req = requests.get(url, params={'itemid': item_id, 'shopid': shop_id})
    req.raise_for_status()

    json_data = json.loads(req.text)
    item = json_data['item']

    if item is None:
        raise exception.NotFoundError("Item not found")

    # time = get_flash_deal_start_time()

    item_data = custom_objects.Item(item['itemid'], item['shopid'], item['name'].strip(), item['price'], datetime.now())

    return item_data

def get_item_list(list):
    url = base_url + '/item/get_list'
    data = {'item_shop_ids': list}
    json_data = json.dumps(data)
    req = requests.post(url, headers={'Content-Type' : 'application/json'}, data=json_data)
    req.raise_for_status()

    result = json.loads(req.text)
    items_data = result['items']
    items = []

    for item in items_data:
        if item is None:
            continue
        items.append(custom_objects.Item(item['itemid'], item['shopid'], item['name'].strip(), item['price'], datetime.now()))

    return items

# #mayb can cache flash deal start time or store in db(TO DO to make it faster when adding item)
# def get_flash_deal_start_time():
#     flash_get_url = base_url + '/flash_sale/get_all_sessions'
#     req = requests.get(flash_get_url)
#     req.raise_for_status()

#     json_data = json.loads(req.text)
#     sessions = json_data['data']['sessions']

#     time = 0

#     for session in sessions:
#         if session['is_ongoing'] == 'true':
#             time = session['start_time']

#     return time

def get_flash_deal_items():
    url = base_url + '/flash_sale/get_items'
    req = requests.get(url)
    flash_items_data = req.json()['data']['items']
    flash_deal_items = []

    for item in flash_items_data:
        item = custom_objects.Item(item['itemid'], item['shopid'], item['name'].strip(), item['price'], datetime.now())
        flash_deal_items.append(item)

    return flash_deal_items

def update_price(item_id, price):
    storage.update_price(item_id, price)

def timestamp_from_datetime(dt):
    ts = time.mktime(dt.timetuple())
    return int(ts)


   




