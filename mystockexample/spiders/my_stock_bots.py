import scrapy
from mystockexample.items import MystockexampleItem

class MyStockBotsSpider(scrapy.Spider):
    name = 'my_stock_bots'
    allowed_domains = ['finance.naver.com/item/sise.nhn?code=005930']
    start_urls = ['https://finance.naver.com/item/sise.nhn?code=005930']

    def parse(self, response):
        title = response.xpath('//*[@id="middle"]/div[1]/div[1]/h2/a/text()').extract()
        price = response.xpath('//*[@id="_nowVal"]/text()').extract()
        volume = response.xpath('//*[@id="_quant"]/text()').extract()
        lowest_price = response.xpath('//*[@id="_low"]/text()').extract()
        highest_price = response.xpath('//*[@id="_high"]/text()').extract()
        
        for row in zip(title, price, volume, lowest_price, highest_price):
            item = MystockexampleItem()
            item['title'] = row[0]
            item['price'] = row[1]
            item['volume'] = row[2]
            item['lowest_price'] = row[3]
            item['highest_price'] = row[4]

            yield item

