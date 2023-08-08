# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import requests
import openpyxl

class DangdangPipeline:
    def open_spider(self, spider):
        # self.datas = []
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = 'dangdang'
        self.sheet.append(('书名', '价格', '作者','评分(100%)','评论人数','评论地址','图书地址','图片地址'))

    def process_item(self, item, spider):
        self.sheet.append((item['title'],item['price'],item['author'],item['star'],item['comment_num'],item['comment_src'],item['src'],item['imgsrc']))
        return item
        # self.datas.append(json.dumps(dict(item), ensure_ascii=False))
        # return item

    def close_spider(self, spider):
        self.wb.save('dangdang.xlsx')
        # with open('dangdang.json', 'a', encoding='utf-8') as f:
        #     json.dump(self.datas, f)

class DangdangDownloadPipeline:

    def process_item(self, item, spider):
        src = item.get('src')
        title = item.get('title')
        filetype = src[src.rfind('.'):]
        resp = requests.get(f'https:{src}')
        if resp.status_code == 200:
            with open(f'imgs/{title}{filetype}', 'wb') as file:
                file.write(resp.content)
        return item