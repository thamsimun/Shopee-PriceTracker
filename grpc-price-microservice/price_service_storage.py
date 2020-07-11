from proto import price_service_pb2
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

config = {'host':'db', 'user':'root', 'password':'Garena.com', 'database':'Price'}
db = mysql.connector.connect(**config)
# db = mysql.connector.connect(
#     host = "db",
#     user = "root",
#     password = "Garena.com",
#     database = "Price"
# )

# dbconfig = {
#     "host" : "C02C97BKMD6M.local",
#     "user" : "root",
#     "password": "Garena.com",
#     "database": "Price"
# }

# cnxpool = mysql.pooling.MySQLConnectionPool(pool_name = "mypool",
#                                                       pool_size = 10,
#                                                       **dbconfig)

# cnxpool = mysql.connector.pooling.MySQLConnectionPool(user="root", password="Garena.com",
#                                   host="db",
#                                   database="Price", pool_name='mypool', pool_size=32)


# if (db):
#     # Carry out normal procedure
#     print "Connection successful"
# else:
#     # Terminate
#     print "Connection unsuccessful"

# if connection_object.is_connected():
#        db_Info = connection_object.get_server_info()
#        print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)

#        cursor = connection_object.cursor()
#        cursor.execute("select database();")
#        record = cursor.fetchone()
#        print ("Your connected to - ", record)

# except Error as e :
#     print ("Error while connecting to MySQL using Connection pool ", e)
# finally:
#     #closing database connection.
#     if(connection_object.is_connected()):
#         cursor.close()
#         connection_object.close()
#         print("MySQL connection is closed")

def item_exist(item_id):
    # db = cnxpool.get_connection()
    cursor = db.cursor()
    query = "SELECT item_id FROM ItemInfo WHERE item_id='%d'" % item_id
    cursor.execute(query)
    data = cursor.fetchone()
    # db.close()
    if data is None:
        return False
    return True

def add_item_details(item):
    # db = cnxpool.get_connection()
    cursor = db.cursor()
    #add into item info table
    query = "INSERT IGNORE INTO ItemInfo (item_id, item_name, shop_id, price) VALUES (%s, %s, %s, %s)"
    values = (item.item_id, item.item_name, item.shop_id, item.price)
    cursor.execute(query,values)
    db.commit()
    # db.close()
    
# def add_flash_items(items):
#     cursor = db.cursor()
#     query = "INSERT INTO FlashSale (promotion_id, item_id, item_name, shop_id, price, time) VALUES (%s, %s, %s, %s, %s, %s)"
#     values = [(item.promotion_id, item.item_id, item.item_name, item.shop_id, item.price, item.time) for item in items]
#     cursor.executemany(query, values)
#     db.commit()

def add_item_price(item):
    # db = cnxpool.get_connection()
    cursor = db.cursor()
    query = "INSERT INTO ItemPrice (item_id, price, time) VALUES (%s, %s, %s)"
    values = (item.item_id, item.price, item.time)
    cursor.execute(query, values)
    db.commit()
    # db.close()

def add_item_price_update(item_id, price, time):
    # db = cnxpool.get_connection()
    cursor = db.cursor()
    query = "INSERT INTO ItemPrice (item_id, price, time) VALUES (%s, %s, %s)"
    values = (item_id, price, time)
    cursor.execute(query, values)
    db.commit()
    # db.close()


def read_item_detail(item_id):
    # db = cnxpool.get_connection()
    cursor = db.cursor(dictionary=True)
    #read item details
    query = "SELECT item_id, item_name, shop_id, price FROM ItemInfo WHERE item_id= '%d'" % item_id
    cursor.execute(query)
    data = cursor.fetchone()
    # db.close()
    return data

def read_all_items():
    # db = cnxpool.get_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT item_id, shop_id FROM ItemInfo"
    cursor.execute(query)
    data = cursor.fetchall()
    # db.close()
    return data

#should i read all the item details at once?
# def read_item_details(item_id):
#     cursor = db.cursor(dictionary=true)
#     #read item details
#     query = "SELECT item_id, item_name, shop_id FROM ItemInfo WHERE item_id= '%d'" % item_id
#     cursor.execute(query)
#     data = cursor.fetchall()
#     return data

# def read_flash_items():
#     cursor = db.cursor(dictionary=True)
#     query = "SELECT promotion_id, item_id, item_name, shop_id, price, time FROM FlashSale"
#     cursor.execute(query)
#     data = cursor.fetchall()
#     return data

# def read_flash_item():
#     cursor = db.cursor(dictionary=True)
#     query = "SELECT promotion_id FROM FlashSale LIMIT 1"
#     cursor.execute(query)
#     data = cursor.fetchall()
#     return data

def read_price_change(item_id):
    # db = cnxpool.get_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT item_id, price, time FROM ItemPrice WHERE item_id = '%d'" %item_id
    cursor.execute(query)
    data = cursor.fetchall()
    # db.close()
    return data

def read_all_items_details(item_ids):
    # db = cnxpool.get_connection()
    cursor = db.cursor(dictionary=True)
    list = []
    for item_id in item_ids:
        query = "SELECT item_id, item_name, shop_id FROM ItemInfo WHERE item_id = '%d'" %item_id
        cursor.execute(query)
        data = cursor.fetchone()
        list.append(data)
    # db.close()
    return list


def update_price(item_id, price):
    # db = cnxpool.get_connection()
    cursor = db.cursor()
    query = "UPDATE ItemInfo SET price = '%s' WHERE item_id = '%s'"
    cursor.execute(query, (price, item_id))
    db.commit()
    # db.close()




