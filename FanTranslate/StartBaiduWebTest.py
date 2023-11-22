# class StartBaiduWeb:
import time

import requests
import win32clipboard

from bs4 import  BeautifulSoup

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class StartBaiduWebTest():
    def clearBtn(self,driver):
        clean = driver.find_element(by=By.CLASS_NAME, value='textarea-clear-btn')
        clean.click()
    def copyBtn(self,driver):
        copybtn = driver.find_element(by=By.CLASS_NAME, value='icon-copy')
        copybtn.click()
        self.sleepTime(1)
        win32clipboard.OpenClipboard()
        context = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return  context
    def sleepTime(self,timenumber):
        time.sleep(timenumber)

    def startFireFox(self,fromlang,tolang):
        driver = webdriver.Firefox()
        # url1 = "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#auto/zh/"
        url1 = f"https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#{fromlang}/{tolang}/"
        # driver.get("https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#jp/zh/")
        print(f"url=={url1}")
        driver.get(url1)
        driver.refresh()
        return driver
    def getTranslateData(self,input,fromlang,tolang,driver):
        try:
            if driver is None:
                driver=self.startFireFox(fromlang,tolang)
            inputText = driver.find_element(by=By.ID, value='baidu_translate_input')
            inputText.send_keys(input)
            self.sleepTime(3)

            data =self.copyBtn(driver)
            if data == "" or data is None:
                data =self.copyBtn(driver)
            # self.sleepTime(timeNumber)
            self.clearBtn(driver)
            return data
        except Exception as e:
            driver.refresh()
            self.sleepTime(4)
            print(f"findelemali {e}")
            self.getTranslateData(input,fromlang,tolang,driver)
        # inputText.clear()



    # if __name__=="__main__":
    #     driver = webdriver.Firefox()
    #     # url="https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#jp/zh/"
    #     # url1="https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=ah#jp/zh/"
    #     driver.get("https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#jp/zh/")
    #     driver.refresh()
    #     timeNumber=2
    #     inputText = driver.find_element(by=By.ID, value='baidu_translate_input')
    #     inputText.send_keys("こんにちは")
    #     sleepTime(timeNumber)
    #     data=copyBtn(driver)
    #     if data =="" or data is None:
    #         data = copyBtn(driver)
    #     sleepTime(timeNumber)
    #     clearBtn(driver)
    #     inputText.send_keys("おはようございます")
    #     sleepTime(timeNumber)
    #     data = copyBtn(driver)
    #     if data == "" or data is None:
    #         data = copyBtn(driver)
    #     sleepTime(timeNumber)
    #     clearBtn(driver)
    #     print(f"复制的值=={data}")
    #     inputText.send_keys("こんばんは ")
    #     sleepTime(timeNumber)
    #     data = copyBtn(driver)
    #     if data == "" or data is None:
    #         data = copyBtn(driver)
    #     sleepTime(timeNumber)
    #     clearBtn(driver)
    #     print(f"复制的值=={data}")
    #     inputText.send_keys("すみません ")
    #     sleepTime(timeNumber)
    #     data=copyBtn(driver)
    #     if data =="" or data is None:
    #         data = copyBtn(driver)
    #     sleepTime(timeNumber)
    #     clearBtn(driver)
    #     print(f"复制的值=={data}")
    #     pass
