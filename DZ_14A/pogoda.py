import requests
import re
import pprint
import json
from bs4 import BeautifulSoup

url='https://www.hmn.ru/index.php?index=8&value=26898&tz=3&start=2022-04-19&fin=2023-04-20&x=15&y=6#range'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
# result = {}
#f='<td align="center" class="m11"><b>'
#news_a = soup.find_all('td')
#print(news_a)

for tag in soup.find_all('td'):
    print(f'{tag.name}: {tag.text}')
# for one_news_a in news_a:
#     text = one_news_a.text
#     href = one_news_a.get('href')
#     # print(text, href)
#     # шаг 2
#     url = f'{domain}{href}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # получаем заголовки
#     news_titles_tag = soup.find_all('strong')
#     titles = []
#     for title_tag in news_titles_tag:
#         # print(title_tag.text)
#         titles.append(title_tag.text)
#
#     # добавим в словарь
#     result[text] = titles
#
#pprint.pprint(result)
#
#
# # session = requests.Session()
# # result = session.get('https://www.hmn.ru/index.php?index=8&value=26898&tz=3&start=2022-04-19&fin=2023-04-20&x=15&y=6#range')
# # print(result.status_code)
# # print(result.json())
# # items = result.json()
# # #items=json.loads(result.text)
# # print(type(items))
# # for item in items:
# #print(items[0])
#
