# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
import pymysql
# class DushuPipeline:
#     def process_item(self, item, spider):
#         return item

class MysqlPipleline:
    def open_spider(self, spider):
        settings = get_project_settings()
        # DB_HOST = 'localhost'
        # DB_PORT = 3306
        # DB_USER = 'root'
        # DB_PASSWORD = 'wangzhiqiang.1'
        # DB_NAME = 'py_spider'
        # DB_CHARSET = 'utf8'
        
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()


    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into dushu(name,src,img_src) values(%s,%s,%s)'
        values = (item["name"], item["src"], item["img_src"])
        self.cursor.execute(sql, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()