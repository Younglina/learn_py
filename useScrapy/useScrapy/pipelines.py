# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class UsescrapyPipeline:
#     def process_item(self, item, spider):
#         return item
import openpyxl

from useScrapy.items import MovieItem

class MovieItemPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = '豆瓣Top250'
        self.sheet.append(('排名','电影名','导演','上映年份','制片国家/地区','分类','评分','评分人数','短评','详情地址','图片地址'))
        
    def process_item(self, item, spider):
        self.sheet.append((item['rank'],item['title'],item['director'],item['years'],item['makers'],item['types'],item['rating_num'],item['rating_peoples'],item['quote'],item['detail_url'],item['img_url']))
        return item
        
    def close_spider(self, spider):
        self.wb.save('豆瓣Top250电影数据.xlsx')
