import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class StartYouDaoWeb():


    def startFireFox(self,fromlang,tolang):
        driver = webdriver.Firefox()
        # url1 = "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#auto/zh/"
        url1 = f"https://m.youdao.com/translate"
        # driver.get("https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#jp/zh/")
        print(f"url=={url1}")
        driver.get(url1)
        selecet = driver.find_element(By.CLASS_NAME, "convert")
        selecet.click()
        selecet.send_keys(3)
        return driver

    def getTranslateData(self, input, fromlang, tolang, driver):
        if driver is None:
            driver = self.startFireFox(fromlang, tolang)

        inputData = driver.find_element(By.ID, "inputText")
        inputData.send_keys(input)
        btnTranslate = driver.find_element(By.CLASS_NAME, "blue-btn")
        btnTranslate.click()
        time.sleep(1)
        btnTranslate1 = driver.find_element(By.ID, "translateResult")
        data = btnTranslate1.__getattribute__("text")
        print(data)
        if data=="" or data is None:
            self.getTranslateData(input, fromlang, tolang, driver)
    pass
