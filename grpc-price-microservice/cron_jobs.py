from datetime import datetime
import os
import price_service_logic

from apscheduler.schedulers.blocking import BlockingScheduler


def price_change_cron():
    try:
        #get unique item ids and shop ids from db to track
        items = price_service_logic.get_all_item_ids()
        print('%d items' % len(items))

        #fetch item data from shopee and add to itemprice db
        item_shop_ids = [{'itemid': x['item_id'], 'shopid': x['shop_id']} for x in items]
        items_data = price_service_logic.get_item_list(item_shop_ids)

        print('%d items fetched from shopee' % len(items_data))

        print('Adding to database')
        for item in items_data:
            item_detail = price_service_logic.get_item_detail(item.item_id)
            print("test")
            price = item_detail['price']
            print(price)
            if price != item.price:
                price_service_logic.add_item_price(item.item_id, item.price, item.time)
                price_service_logic.update_price(item.item_id, item.price)
        
    except Exception as err:
        print(err)

    try:
        print('Fetching flash deal items')
        flash_deal_items = price_service_logic.get_flash_deal_items()
        print("%d items fetched " % len(flash_deal_items))
        print('Saving to database')
        for item in flash_deal_items:
            price_service_logic.add_item_flash(item)
    except Exception as err:
        print(err)



if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(price_change_cron, 'interval', minutes=15)
    # scheduler.add_job(flash_change_cron, 'interval', seconds=60)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass