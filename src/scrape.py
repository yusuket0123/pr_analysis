"""
webscraping
"""

import requests
from bs4 import BeautifulSoup



site = requests.get("https://note.com/k_three")
data = BeautifulSoup(site.text, "html.parser")

print(data.title)
print(data.title.text)
