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

### サイトにアクセス
url = "https://prtimes.jp/main/html/searchrlp/company_id/23382"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

### 「もっとみる」ボタンは現状ないが、今後ページに現れる可能性あり？

### サイトの記事URLを取得
tags = driver.find_elements_by_css_selector("article > h3 > a")
urls = list()
for tag in tags:
    url = tag.get_attribute("href")
    urls.append(url) # 記事のurl取得
    print(url)
time.sleep(2)

url = urls[1]
soap = requests.get(url)
site = bs4(soap.text, "html.parser")

print(site.find_all("div", attrs = {"class": re.compile("(r-head)|(rich-text)")}))
print(site.find_all("a", attrs={"href": re.compile(".topics.keywords.*")}))
print(site.select("p > span > img"))
print(site.select(".information-release > time"))
time.sleep(2)

"""like数
url_like = site.find("div", class_="fb-like").get("data-href")
soap_like = requests.get(url_like)
site_like = bs4(soap_like.text, "html.parser")
print(site_like)

iframe_src = soup.select_one(".div.fb-like").attrs["src"]
r = s.get(f"https:{iframe_src}")
soup = BeautifulSoup(r.content, "html.parser")
"""
"""該当箇所iframe
<iframe name="f3f4e30c1da0084" width="80px" height="1000px" data-testid="fb:like Facebook Social Plugin" title="fb:like Facebook Social Plugin" frameborder="0" allowtransparency="true" allowfullscreen="true"
scrolling="no" allow="encrypted-media"
src="https://www.facebook.com/v2.9/plugins/like.php?action=like&amp;app_id=1495958567142613&amp;channel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df392798d4759efc%26domain%3Dprtimes.jp%26origin%3Dhttps%253A%252F%252Fprtimes.jp%252Ff2684a789ab3948%26relation%3Dparent.parent&amp;container_width=92&amp;href=https%3A%2F%2Fprtimes.jp%2Fmain%2Fhtml%2Frd%2Fp%2F000000051.000023382.html&amp;layout=box_count&amp;locale=ja_JP&amp;sdk=joey&amp;share=true&amp;size=small&amp;width=80"
style="border: none; visibility: visible; width: 92px; height: 72px;" class=""></iframe>
"""
"""
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
        "content": site.find_all("div", attrs = {"class": re.compile("(r-head)|(rich-text)"))}), \
        "keywords": site.find_all("a", attrs={"href": re.compile(".topics.keywords.*")}), \
        "images": site.select("p > span > img"), \
        "likes": site.find("span", attrs = {"id": "u_0_1"}), \
        "time": site.select(".information-release > time") \
    }
    # 記事ごとに要素を格納
    dict_pages[title] = dict_elems
    print("------- \n------- \n done \n------- \n-------")
    time.sleep(2)

"""
