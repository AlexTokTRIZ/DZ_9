import requests
import pprint
import json

session = requests.Session()
result = session.get('https://www.hmn.ru/index.php?index=8&value=26898&tz=3&start=2022-04-19&fin=2023-04-20&x=15&y=6#range')
print(result.status_code)
print(result.text)
#items = result.json()