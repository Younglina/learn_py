# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
    star = scrapy.Field()
    comment_num = scrapy.Field()
    comment_src = scrapy.Field()
    src = scrapy.Field()
    imgsrc = scrapy.Field()
    pass
