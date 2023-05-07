import requests
import pprint
import json
from collections.abc import MutableMapping


def _flatten_dict_gen(d, parent_key, sep):
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            yield from flatten_dict(v, new_key, sep=sep).items()
        else:
            yield new_key, v
def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str = '.'):
    return dict(_flatten_dict_gen(d, parent_key, sep))

session = requests.Session()
result = session.get('https://geocode-maps.yandex.ru/1.x?apikey=3f74eb93-519d-4a53-a0ca-cedb57c20fab&geocode=москва,+проспект мира,+101&format=json')

print(result.status_code)
print(result.json())
items = result.json()
#items=json.loads(result.text)
print(type(items))
# for item in items:
k=list(items)[0]
print(items.values())
print(flatten_dict(items))

# for k,v in items.items():
#     for _k, _v in k.items:
#         print(_v)


# запрос на геокодирование
#https: // yandex.ru / dev / maps / geocoder / doc / desc / concepts / input_params.html