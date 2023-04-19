from bs4 import BeautifulSoup
import requests
import os
import re

def parse():
    url = 'https://омгту.рф/general_information/news/?PAGEN_1='
    max_pages = 157
    file = open("spisok.txt", 'w', encoding="utf-8")



    for p in range(max_pages):
        cur_url = url + str(p + 1)
        print("Парсинг страницы №: %d" % (p+1))
        page = requests.get(cur_url)
        print(page.status_code)
        news_list = BeautifulSoup(page.text, "html.parser")
        name = news_list.findAll('div', class_='news-list')
        news_names = ''
        for news in name:
            if news.find('b'):
                news_names=news.text
                sep = 'Новости \n'
                news_names = news_names.split(sep, 1)[0]
                file.write(news_names)



    with open("spisok.txt", 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = list(filter(lambda x: not re.match(r'^s*$', x), lines))
    with open("spisok.txt", 'w', encoding='utf-8') as file:
        file.writelines(lines)
