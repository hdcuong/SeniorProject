
import scrapy


class CrawlItem(scrapy.Item):
  
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    screen = scrapy.Field()
    cpu = scrapy.Field()
    ram = scrapy.Field()
    graphics = scrapy.Field()
    os = scrapy.Field()
    weight = scrapy.Field()
    link = scrapy.Field()
    pass
