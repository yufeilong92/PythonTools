# class StartBaiduWeb:
import time

import requests
import win32clipboard

from bs4 import  BeautifulSoup

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

def clearBtn(driver):
    clean = driver.find_element(by=By.CLASS_NAME, value='textarea-clear-btn')
    clean.click()
def copyBtn(driver):
    copybtn = driver.find_element(by=By.CLASS_NAME, value='icon-copy')
    copybtn.click()
    sleepTime(1)
    win32clipboard.OpenClipboard()
    context = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return  context
def sleepTime(timenumber):
    time.sleep(timenumber)

if __name__=="__main__":
    driver = webdriver.Firefox()
    # url="https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#jp/zh/"
    # url1="https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=ah#jp/zh/"
    # url1="https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#auto/zh/"
    url="https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#jp/zh/"
    driver.get(url)
    driver.refresh()
    timeNumber = 2
    inputText = driver.find_element(by=By.ID, value='baidu_translate_input')
    inputText.send_keys("こんにちは")
    sleepTime(timeNumber)
    data = copyBtn(driver)
    if data == "" or data is None:
        data = copyBtn(driver)
    # sleepTime(timeNumber)
    clearBtn(driver)
    print(f"复制的值=={data}")
    inputText.send_keys("你好")
    sleepTime(timeNumber)
    data = copyBtn(driver)
    if data == "" or data is None:
        data = copyBtn(driver)
    # sleepTime(timeNumber)
    clearBtn(driver)
    print(f"复制的值=={data}")
    inputText.send_keys("こんばんは ")
    sleepTime(timeNumber)
    data = copyBtn(driver)
    if data == "" or data is None:
        data = copyBtn(driver)
    # sleepTime(timeNumber)
    clearBtn(driver)
    print(f"复制的值=={data}")
    inputText.send_keys("すみません ")
    sleepTime(timeNumber)
    data = copyBtn(driver)
    if data == "" or data is None:
        data = copyBtn(driver)
    # sleepTime(timeNumber)
    clearBtn(driver)
    print(f"复制的值=={data}")
    pass
