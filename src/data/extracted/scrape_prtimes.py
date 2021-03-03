"""
note記事のスクレイピング
*googlecrome環境

pip install bs4
pip install selenium
brew install chromedriver
"""

import requests
import os
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import time
import re
from scrape_func import *

### サイトにアクセス
get_url(url = "https://prtimes.jp/main/html/searchrlp/company_id/23382")
time.sleep(5)

### 「もっとみる」ボタンは現状ないが、今後ページに現れる可能性あり？

### サイトの記事URLを取得
tags = driver.find_elements_by_css_selector("article > h3 > a")
urls = list()
for tag in tags:
    url = tag.get_attribute("href")
    urls.append(url) # 記事のurl取得
    print(url)
time.sleep(5)

time.sleep(5)
# prtimesのいいね数はfb pluginのため取得できない（スクレイピング禁止）

### 各urlにアクセス
# 要素取得
def combine_elem(elements):
    result = ""
    for elem in elements:
        elem_to_text = elem.get_text()
        elem_to_text = re.sub("(\n)|(\r)|(\\u3000)|(\\xa0)|(\s*))", "", elem_to_text) # 改行コードなど削除
        result = result + elem_to_text
    return result

dict_pages = dict()
num = 0
for url in urls:
    num += 1
    soap = requests.get(url)
    site = bs4(soap.text, "html.parser") # 第二引数はparser(解析方法)を指定
    # 要素を取得し、辞書型で格納（本文,#,画像,いいね数,投稿時間の順番）
    # タイトル
    elements_title = site.find_all(attrs = {"class": re.compile("(release--title)|(release--sub_title)")})
    print(elements_title)
    # 本文
    elements_content = site.find_all("div", attrs = {"class": re.compile("(r-head)|(rich-text)")})
    print(elements_content)
    dict_elems = {
        "title": combine_elem(elements = elements_title), \
        "content": combine_elem(elements = elements_content), \
        "keywords": [c.string for c in site.select("dd > ul > li > a")], \
        "images": site.select("p > span > img"), \
        "time": site.find("time")["datetime"] \
    }

    # 記事ごとに要素を格納
    name = "article_note_" + str(num)
    dict_pages[name] = dict_elems
    print(name)
    print(dict_elems)
    print("------- \n------- \n done \n------- \n-------")
    time.sleep(5)
