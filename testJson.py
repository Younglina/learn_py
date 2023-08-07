import json
import requests

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# 将数据写入文件
# with open("assets/data.json", "w") as file:
#     json.dump(data, file)

# # 将数据读出
# with open("assets/data.json", "r") as file:
#     print(json.load(file))

# resp = requests.get('http://is.snssdk.com/api/news/feed/v51/')
# if resp.status_code == 200:
#     data_model = resp.json()
#     for ds in data_model['data']:
#         content = json.loads(ds['content'])
#         print(content['title'])

# import csv
# import random

# with open('scores.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     for name in names:
#         scores = [name]
#         scores += [random.randrange(50, 101) for _ in range(3)]
#         # scores.insert(0, name)
#         writer.writerow(scores)