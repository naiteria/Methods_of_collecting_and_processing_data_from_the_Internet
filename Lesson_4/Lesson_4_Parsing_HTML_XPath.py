# 1. Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# 2. Сложить собранные новости в БД

from lxml import html
from pprint import pprint
import requests
from pymongo import MongoClient

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  '(XHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
response = requests.get('https://lenta.ru/', headers=header)
dom = html.fromstring(response.text)

items = dom.xpath('//div[@class = "b-yellow-box__wrap"]/div[@class = "item"]')

a = 'https://lenta.ru'
news = []
for item in items:
    structure = {}
    news_source = 'https://lenta.ru/'
    news_1 = item.xpath('.//a/text()')
    news_1 = " ".join(news_1[0].split())
    link_1 = item.xpath('.//a/@href')
    link = a + link_1[0]
    date = '/'.join(link_1[0].split('/')[2:5])

    structure['название источника'] = news_source
    structure['наименование новости'] = news_1
    structure['ссылка на новость'] = link
    structure['дата публикации'] = date
    news.append(structure)
pprint(news)

client = MongoClient('localhost', 27017)
db = client['Lesson_4']
my = db.my
# my.insert_many(news)
for i in my.find():
    print(i)
