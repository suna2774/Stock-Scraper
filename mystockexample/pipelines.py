# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MystockexamplePipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()

    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root',password='',db='mydb',charset='utf8',port=3306)
        self.cur = self.conn.cursor()
        print("DB Connected")

    def createTable(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            price VARCHAR(100),
            volume VARCHAR(20),
            lowest_price VARCHAR(20),
            highest_price VARCHAR(20),
            created_at DATETIME DEFAULT NOW()
        )''')

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        title = item.get('title','').strip()
        price = item.get('price','').strip()
        volume = item.get('volume','').strip()
        lowest_price = item.get('lowest_price','').strip()
        highest_price = item.get('highest_price','').strip()

        sql = "INSERT INTO stock(title,price,volume,lowest_price,highest_price) VALUES(%s,%s,%s,%s,%s)"
        self.cur.execute(sql, (title, price, volume, lowest_price, highest_price))
        self.conn.commit()
        