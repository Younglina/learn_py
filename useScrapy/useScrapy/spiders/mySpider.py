import scrapy
import re
from scrapy import Request
from useScrapy.items import MovieItem

class MyspiderSpider(scrapy.Spider):
    name = "mySpider"
    allowed_domains = ["movie.douban.com"]

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}')

    def parse(self, response):
        movie_items = response.css('.grid_view .item')
        for movie in movie_items:
            item = MovieItem()
            item['rank'] = movie.css('.pic em::text').get()
            item['title'] = movie.css('.hd a .title::text').extract_first()
            extInfo = movie.css('.bd p::text').extract()
            item['director'] = re.findall(r"导演:\s*(.*?)\s", movie.css('.bd p::text').extract()[0])[0]
            item['years'],item['makers'],item['types'] = extInfo[1].strip().split('\xa0/\xa0')
            item['rating_num'] = movie.css('.rating_num::text').extract_first()
            item['rating_peoples'] = re.findall(r'\d+', movie.css('.star span ::text')[-1].extract())[0]
            item['quote'] = movie.css('.quote .inq::text').get()
            item['detail_url'] = movie.css('.pic a::attr(href)').get()
            item['img_url'] = movie.css('.pic img::attr(src)').get()
            yield item
