"""
scrapingのための関数クラス
"""

__all__ = ["get_url"]

def get_url(url):
    url = url
    driver = webdriver.Chrome()
    driver.get(url)
