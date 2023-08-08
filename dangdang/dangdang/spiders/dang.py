import scrapy
import re
from dangdang.items import DangdangItem

class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com/cp01.54.00.00.00.00.html"]
    start_urls = ["https://category.dangdang.com/cp01.54.00.00.00.00.html"]

    def parse(self, response):
        books = response.css('#component_59 li')
        for bk_item in books:
            book = DangdangItem()
            book['title'] = bk_item.css('.pic::attr(title)').get()
            book['src'] = 'https:' + bk_item.css('.pic::attr(href)').get()
            book['author'] = bk_item.css('.search_book_author span a::attr(title)').get()
            search_star_line = bk_item.css('.search_star_line')
            print(search_star_line.css('span'))
            if len(search_star_line.css('span'))>0:
                book['star'] = re.findall(r"width:\s*(.*?);", search_star_line.css('.search_star_black span::attr(style)').get())[0]
                book['comment_num'] = bk_item.css('.search_comment_num::text').get()
                book['comment_src'] = 'https:' + bk_item.css('.search_comment_num::attr(href)').get()
            imgsrc = bk_item.css('.pic img::attr(data-original)').get()
            if imgsrc is None:
                imgsrc = bk_item.css('.pic img::attr(src)').get()
            book['imgsrc'] = 'https:' + imgsrc
            book['price'] = bk_item.css('.search_now_price::text').get()
            # 获取以后交给piplines
            yield book
