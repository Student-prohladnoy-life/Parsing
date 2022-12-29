import requests
import pprint

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f"{DOMAIN}vacancies"

# params = {
#     'text': 'C# developer',
#     # Страница
#     'page': 1
# }
#
# result = requests.get(url_vacancies, params=params).json()
#
# #print(result.status_code)
# #pprint.pprint(result.json())
#
# items = result["items"]
#
# first = items[0]
#
# #pprint.pprint(first)
#
# # print(first["alternate_url"])
# # print(first["url"])
# one_vacancy_url = first["url"]
#
# result = requests.get(one_vacancy_url, params=params).json()
#
# pprint.pprint(result)


params = {
    'text': 'NAME:(Python OR Java)'
            'AND COMPANY_NAME:(LIFE PAY OR Procter & Gamble OR Yandex OR Growth.pet)'
            'AND (Django OR Spring OR SQL OR FastAPI OR SQLite OR Git)',
    'page': 1
}

result = requests.get(url_vacancies, params=params).json()
pprint.pprint(result)
print(result['found'])
print(result['items'])