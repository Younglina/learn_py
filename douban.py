import bs4
import requests
import json

movie_data = []
for page in range(1, 2):
  url = f'https://movie.douban.com/top250?start={(page-1)*25}'
  resp = requests.get(
    url,
    headers={'User-Agent': 'BaiduSpider'}
  )
  soup = bs4.BeautifulSoup(resp.text, 'html.parser')
  movie_list = soup.find_all('div', class_='item')
  for movie in movie_list:
    title = movie.find('span', class_='title').text
    rating = movie.find('span', class_='rating_num').text
    movie_data.append({'title': title, 'rating': rating})

with open('douban.json', 'w', encoding='utf-8') as f:
  json.dump(movie_data, f, ensure_ascii=False, indent=4)