import requests
import os
import re

def down_img(filename, url):
    resp = requests.get(url)
    filename2 = re.findall(r"\w+", filename)
    filetype = url[url.rfind('.'):]
    if resp.status_code == 200:
      with open(f'threadP/images/beauty/{filename2}{filetype}', 'wb') as file:
         file.write(resp.content)

def main():
   if not os.path.exists('threadP/images/beauty'):
      os.makedirs('threadP/images/beauty')
   for page in range(3):
      resp = requests.get(f'https://image.so.com/zjl?sn={page*30}&ch=beauty&t1=625')
      if resp.status_code == 200:
         list_data = resp.json()['list']
         for pic in list_data:
            down_img(pic['pic_desc'], pic['qhimg_url'])

main()