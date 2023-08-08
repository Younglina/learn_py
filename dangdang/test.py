import json
from dangdang.items import DangdangItem

book = DangdangItem()
book['title'] = '啊开始讲课了'
book['src'] = '发生'
book['price'] = 'price'


print()
with open('test.json', 'a', encoding='utf-8') as f:
  json.dump([json.dumps(dict(book), ensure_ascii=False)], f)
  