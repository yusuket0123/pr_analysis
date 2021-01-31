"""
note記事のスクレイピング
*googlecrome環境

pip install bs4
pip install selenium
brew install chromedriver
"""

import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time

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
    time.sleep(3)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("new_height: {}".format(new_height))
    if new_height == old_height:
        i += 1
        print("i: {}".format(i))
    else:
         i = 0
    if i == 3: # ネット環境で3秒以内にサイトをリロードできない可能性があるため３回の猶予を持たせる
        break # これ以上スクロールで新たにロードされる情報がなくなったら処理を停止

### サイトの記事URLを取得
tags = driver.find_elements_by_css_selector(".renewal-p-cardItem__title > a")
list_url = list()
for tag in tags:
    url = tag.get_attribute("href")
    list_url = list_url.append(url) # 記事のurl取得
    print("url: {}".format(url))
