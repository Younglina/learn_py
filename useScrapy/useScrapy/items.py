# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    rank = scrapy.Field() # 排名
    title = scrapy.Field() # 电影名
    director = scrapy.Field() # 导演
    years = scrapy.Field() # 上映年份
    makers = scrapy.Field() # 制片国家/地区
    types = scrapy.Field() # 分类
    rating_num = scrapy.Field() # 评分
    rating_peoples = scrapy.Field() # 评分人数
    quote = scrapy.Field() # 短评
    detail_url = scrapy.Field() # 详情地址
    img_url = scrapy.Field() # 图片地址
