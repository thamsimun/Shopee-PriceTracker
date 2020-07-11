class Item(object):
    def __init__(self, item_id, shop_id, item_name, price, time):
        self.item_id = item_id
        self.shop_id = shop_id
        self.item_name = item_name
        self.price = price
        self.time = time

    def __repr__(self):
        return 'item_id: {}, shop_id: {}, name: {}, price: {}, time: {}'\
            .format(self.item_id, self.shop_id, self.item_name.encode('utf-8'), self.price, self.time)
