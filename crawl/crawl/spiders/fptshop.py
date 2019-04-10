import scrapy
import csv
from crawl.items import CrawlItem
from scrapy_splash import SplashRequest
f = csv.writer(open('fpt.csv', 'w'))
f.writerow(['Name', 'Price', 'Image', 'Screen', 'CPU', 'RAM', 'Graphics', 'OS', 'Weight', 'Link'])



class FptShopSpider(scrapy.Spider):

    name = "fpt"
    allowed_domains = ['fptshop.com.vn']
    start_urls = ["https://fptshop.com.vn/may-tinh-xach-tay/dell?sort=ban-chay-nhat&trang=1", "https://fptshop.com.vn/may-tinh-xach-tay/dell?sort=ban-chay-nhat&trang=2","https://fptshop.com.vn/may-tinh-xach-tay/dell?sort=ban-chay-nhat&trang=3","https://fptshop.com.vn/may-tinh-xach-tay/apple-macbook", "https://fptshop.com.vn/may-tinh-xach-tay/msi", "https://fptshop.com.vn/may-tinh-xach-tay/asus", "https://fptshop.com.vn/may-tinh-xach-tay/asus?sort=ban-chay-nhat&trang=2", "https://fptshop.com.vn/may-tinh-xach-tay/asus?sort=ban-chay-nhat&trang=3", "https://fptshop.com.vn/may-tinh-xach-tay/hp", "https://fptshop.com.vn/may-tinh-xach-tay/hp?sort=ban-chay-nhat&trang=2", "https://fptshop.com.vn/may-tinh-xach-tay/hp?sort=ban-chay-nhat&trang=3", "https://fptshop.com.vn/may-tinh-xach-tay/masstel", "https://fptshop.com.vn/may-tinh-xach-tay/acer", "https://fptshop.com.vn/may-tinh-xach-tay/lenovo", "https://fptshop.com.vn/may-tinh-xach-tay/haier-hr-13mz-pentium-n4200"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse)

    def parse(self, response):
        item = CrawlItem()
        for data in response.xpath("//div[@class='fs-lapitem']"):
            item["name"] = data.xpath("./div/div[1]/h3/a/span/text()").extract_first()
            item["price"] = data.xpath("./div/div[1]/div[1]/p/text()").extract_first()
            item["image"] = data.xpath("./a/p/img/@data-original").extract_first()
            # item["image"] = data.xpath("./a/p/img/@src").extract_first()
            if item["image"] == None:
                item["image"] = data.xpath("./a/p/img/@src").extract_first()
                # item["image"] = data.xpath("./a/p/img/@data-original").extract_first()
            item["screen"] = data.xpath("./div/div[2]/ul/li[1]/text()").extract_first()
            item["cpu"] = data.xpath("./div/div[2]/ul/li[2]/text()").extract_first()
            item["ram"] = data.xpath("./div/div[2]/ul/li[3]/text()").extract_first()
            item["graphics"] = data.xpath("./div/div[2]/ul/li[4]/text()").extract_first()
            item["os"] = data.xpath("./div/div[2]/ul/li[5]/text()").extract_first()
            item["weight"] = data.xpath("./div/div[2]/ul/li[6]/text()").extract_first()
            item["link"] ="https://fptshop.com.vn/" + data.xpath("./a/@href").extract_first()
            f.writerow([item["name"], item["price"], item["image"], item["screen"], item["cpu"], item["ram"], item["graphics"], item["os"], item["weight"], item["link"]])
            yield item