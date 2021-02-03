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

"""
ページにいく
「ページでもっとみる」クリック
最下部へのスクロールを記事が尽きるまでループ
各記事にアクセス
必要な要素を取ってくる
理想: リファクタリングで関数化
"""



### サイトにアクセス
url = "https://note.com/k_three"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

### もっとみる　クリック（note特有）
button = driver.find_element_by_css_selector(".o-timelineHome__more > button")
button.click()
time.sleep(3)

### スクロール（note特有）
new_height = driver.execute_script("return document.body.scrollHeight") # ページ長さ取得
i = 0
while True:
    old_height = new_height
    print("old_height: {}".format(old_height))
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # ページ最下までスクロール
    # Wait to load page
    time.sleep(3) # ロードのための3秒間の猶予
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("new_height: {}".format(new_height))
    if new_height == old_height:
        i += 1
        print("i: {}".format(i))
    else:
         i = 0
    if i == 3: # ネット環境により3秒以内にサイトをリロードできない可能性があるため３回の猶予を持たせる
        break # これ以上スクロールで新たにロードされる情報がなくなったら処理を停止

### サイトの記事URLを取得
tags = driver.find_elements_by_css_selector(".renewal-p-cardItem__title > a")
urls = list()
for tag in tags:
    url = tag.get_attribute("href")
    urls.append(url) # 記事のurl取得
    print(url)
print(urls)

### 各urlにアクセス
# 要素取得
dict_pages = dict()
for url in urls:
    soap = requests.get(url)
    site = bs4(soap.text, "html.parser") # 第二引数はparser(解析方法)を指定
    # 要素を取得し、辞書型で格納（本文,#,画像,いいね数,投稿時間の順番）
    title = site.title.text
    print(title)
    dict_elems = {
        "content": site.find_all("p", attrs = {"name": re.compile(".....")}), \
        "hashtags": site.find_all(attrs={"class": "a-tag__label"}), \
        "images": site.select(".lazyload"), \
        "likes": site.select(".o-noteContentText__likeCount"), \
        "time": site.select(".o-noteContentHeader__date") \
    }
    # 記事ごとに要素を格納
    dict_pages[title] = dict_elems
    print("------- \n------- \n done \n------- \n-------")

"""
soap = requests.get(urls[1])
site = bs4(soap.text, "html.parser")
print(site.find_all("p", attrs = {"name": re.compile(".....")})) # regexでattributesを検索
print(site.find_all(attrs={"class": "a-tag__label"}))
#print(site.select(".o-noteContentText__body > p")) # 本文（文字数、筆者）
#print(site.select(".a-tag__label")) # ハッシュタグ（数、ハッシュダグの言葉）
print(site.select(".lazyload")) # 画像
print(site.select(".o-noteContentText__likeCount")) # like
print(site.select(".o-noteContentHeader__date")) # 投稿時間
"""
