#!/usr/bin/env python3

# Copyright (c) 2020, Suzuki Taisei.
# All rights reserved.
#
# $Id: kg_lib.py,v 1.32 2020/03/25 07:50:31 suzuki

from pyfzf.pyfzf import FzfPrompt
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

fzf = FzfPrompt()


class Driver(object):
    def __init__(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(options=option)

    def all_operate(self):
        self.driver_operate()
        self.switch_window()
        self.printing()
        self.quiting()

    def driver_operate(self):
        self.driver.get('https://library.kwansei.ac.jp/')
        self.driver.find_element_by_xpath(
            "//*[@id='words']").send_keys(self.inputs())
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[1]/div/ul[2]/li[1]/form/input[3]").click()
        time.sleep(1)

    def inputs(self):
        return input("choose book title or word -> ")

    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)

    def printing(self):
        elements = self.driver.find_elements_by_class_name("opac_book_title")
        x = fzf.prompt([element.text for element in elements])
        print(x)

    def quiting(self):
        self.driver.quit()
        sys.exit()


def main():
    driver = Driver()
    driver.all_operate()


main()
