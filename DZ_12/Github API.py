#Auth on Git
#Поиск кода, использующего pygame
token="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"

import requests
import pprint

session = requests.Session()
session.auth = ('AlexTokTRIZ', token)

result = session.get('https://api.github.com/search/code?q=pygame+in:file+language:python')
print(result.status_code)
items = result.json()['items']

for item in items:
    if not item['path'].startswith('venv'):
        pprint.pprint(item)



# Получение репозиториев
# result = requests.get('https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc')
# pprint.pprint(result.json()['total_count'])
# params = {
#     'q': 'tetris+language:assembly',
#     'sort': 'stars',
#     'order': 'desc'
# }
# result = requests.get('https://api.github.com/search/repositories', params=params)
# print(result.url)
# pprint.pprint(result.json()['total_count'])

# Поиск кода
# https://api.github.com/search/code?q=addClass+in:file+language:js+repo:jquery/jquery

# Авторизация
# 1.
# result = requests.get('https://api.github.com/search/code?q=addClass+in:file+language:js+repo:jquery/jquery', auth=('DanteOnline', token))
# 2.
# headers = {
#     'Authorization': f'token {token}'
# }
# result = requests.get('https://api.github.com/search/code?q=addClass+in:file+language:js+repo:jquery/jquery', headers=headers)
