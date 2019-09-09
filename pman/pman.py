#!/usr/local/bin/python3.7
import urllib.request
from perl import getopts
from bs4 import BeautifulSoup

opt = getopts("u:")
url = "https://docs.python.org/ja/3/library/"

if opt.u:
    url = url + opt.u + ".html"
else:
    pass

html = urllib.request.urlopen(url)
target = BeautifulSoup(html.read(), "lxml")
text_data = str("")
for text in (target.find_all(text=True)):
    text_data = text_data + text
print(text_data.strip())
