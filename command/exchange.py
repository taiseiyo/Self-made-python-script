#!/usr/bin/env python3
from urllib import request
from bs4 import BeautifulSoup
import argparse

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
}


def html_parse():
    url = "https://www.smbc.co.jp/ex/ExchangeServlet?ScreenID=real"
    url = request.Request(url, headers=headers)
    html = request.urlopen(url)
    target = BeautifulSoup(html.read(), "lxml")
    html.close()
    return target


def exchange_rate(target):
    doc = ""
    remove_list = ""
    for line in target.find_all(text=True):
        doc = doc+line

    doc = list(doc.strip().split("\n"))
    for count, i in enumerate(doc):
        if i in remove_list:
            doc.pop(count)

    return doc


def choose_word(word):
    word = word[0]
    if(word == "euro"):
        word = "ユーロ（1 EUR）"
    elif(word == "doll"):
        word = "米ドル（1 USD）"
    else:
        word = "英ポンド（1 GBP）"
    return word


def choose_rate(doc, c_word):
    for count, word in enumerate(doc):
        if(word == c_word):
            print(word)
            print(doc[count+1] + " 円->外")
            print(doc[count+2] + " 外->円")


def parsers():
    parser = argparse.ArgumentParser(description="choice unit of money")
    parser.add_argument("-c", "--choice", nargs='+',
                        help='choice unit of money')
    opt = parser.parse_args()
    return opt


def main():
    opt = parsers()
    target = html_parse()
    doc = exchange_rate(target)
    word = choose_word(opt.choice) \
        if opt.choice else None
    choose_rate(doc, word)


main()
