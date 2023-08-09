import scrapy
from dushu.items import DushuItem

class ItbooksSpider(scrapy.Spider):
    name = "itBooks"
    allowed_domains = ["www.dushu.com"]

    def start_requests(self):
        for page in range(1,100):
            yield scrapy.Request(url=f'https://www.dushu.com/book/1107_{page}.html')

    def parse(self, response):
        dushu = DushuItem()
        books = response.css('.book-info')
        for book in books:
            dushu['name'] = book.css('h3 a::attr(title)').get()
            dushu['src'] = 'https://www.dushu.com'+book.css('.img152 a::attr(href)').get()
            dushu['img_src'] = book.css('.img152 img::attr(data-original)').get()
            yield dushu
