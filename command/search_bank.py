#!/usr/local/bin/python3.7
#!coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import argparse
import time
import datetime
import re

# ID
shop_id = "*******"
bank_id = "*******"
url = "***********"
password = "******"


def control_bank():  # ok
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element_by_xpath("// *[@id='S_BRANCH_CD']").send_keys(shop_id)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='S_ACCNT_NO']").send_keys(bank_id)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='PASSWORD']").send_keys(password)
    time.sleep(1)

    actions = ActionChains(browser)
    browser.execute_script("window.scrollTo(0, 600);")
    actions.move_to_element(browser.find_element_by_xpath(
        "/html/body/form/div[5]/div[2]/div[2]/p[1]/a")).perform()

    time.sleep(1)
    browser.find_element_by_xpath(
        "/html/body/form/div[5]/div[2]/div[3]/input[7]").click()
    time.sleep(2)
    browser.find_element_by_xpath(
        "/html/body/form/div[5]/div/div[3]/ul/li/input").click()
    time.sleep(1)
    tmp = browser.find_element_by_xpath(
        "/html/body/div[3]/div[3]/div/div[3]/div[2]/form/div/div/div[2]/div[2]/table/tbody/tr/td[1]/p[1]/span[2]").text
    browser.close()
    tmp = tmp[:-2]
    text = str(datetime.date.today()) \
        + ":" + str(tmp)
    return text


def files(text):  # ok
    if(text != None):
        f = open("bank.txt", "a")
        print(text, file=f)
        f = open("bank.txt", "r")
        text = f.read()
        print(text)
        f.close()
    else:
        pass


def cal():  # ok
    pattern = "\d*-\d*-\d*:(\d*)"
    past = []
    f = open("bank.txt", "r")
    f = f.read().strip().replace(",", "")
    f = f.split()
    for line in f[-2:]:
        m = re.search(pattern, line)
        past.append(int(m.group(1)))

    print("Balance of the month is " +
          str(past[0] - past[1]))


def parsers():  # ok
    parser = argparse.ArgumentParser(
        description="You can choice \
        execute control_bank")
    parser.add_argument(
        "-e", "--exe", action="store_true",
        help="execute control_bank"
    )
    parser.add_argument(
        "-c", "--cal", action="store_true",
        help="calculate profit and loss  per one month"
    )
    opt = parser.parse_args()
    return opt


def main():
    opt = parsers()
    text = [control_bank() if
            opt.exe == True else None]
    files(text[0])
    cal() if (opt.cal == True) else None

main()
