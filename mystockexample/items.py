# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MystockexampleItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
    lowest_price = scrapy.Field()
    highest_price = scrapy.Field()
    
