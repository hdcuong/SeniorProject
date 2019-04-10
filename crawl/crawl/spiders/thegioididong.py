import scrapy
import csv
from crawl.items import CrawlItem
from scrapy_splash import SplashRequest
f = csv.writer(open('tgdd.csv', 'w'))
f.writerow(['Name', 'Price', 'Image', 'Screen', 'CPU', 'RAM', 'Graphics', 'OS', 'Weight', 'Link'])

class ThegioididongSpider(scrapy.Spider):
    
    name = "tgdd"
    allowed_domains = ['thegioididong.com']
    start_urls = ["https://www.thegioididong.com/laptop-dell","https://www.thegioididong.com/laptop-asus", "https://www.thegioididong.com/laptop-hp-compaq", "https://www.thegioididong.com/laptop-acer", "https://www.thegioididong.com/laptop-acer", "https://www.thegioididong.com/laptop-lenovo", "https://www.thegioididong.com/laptop-msi"]
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse)

    def parse(self, response):
        item = CrawlItem()
        for data in response.xpath("//li[@class='laptop']"):
            item["name"] = data.xpath("./a/h3/text()").extract_first()
            item["price"] = data.xpath("./a/div[1]/strong/text()").extract_first()
            item["image"] = data.xpath("./a/img/@data-original").extract_first()
            if item["image"] == None:
                item["image"] = data.xpath("./a/img/@src").extract_first()
            item["screen"] = data.xpath("./a/figure/span[1]/text()").extract_first()
            item["cpu"] = data.xpath("./a/figure/span[2]/text()").extract_first()
            item["ram"] = data.xpath("./a/figure/span[3]/text()").extract_first()
            item["graphics"] = data.xpath("./a/figure/span[4]/text()").extract_first()
            item["os"] = data.xpath("./a/figure/span[5]/text()").extract_first()
            item["weight"] = data.xpath("./a/figure/span[6]/text()").extract_first()
            item["link"] ="https://www.thegioididong.com" + data.xpath("./a/@href").extract_first()
            f.writerow([item["name"], item["price"], item["image"], item["screen"], item["cpu"], item["ram"], item["graphics"], item["os"], item["weight"], item["link"]])
            yield item