import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class StartYouDaoWeb():


    def startFireFox(self,index):
        driver = webdriver.Firefox()
        # url1 = "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#auto/zh/"
        url1 = f"https://m.youdao.com/translate"
        # driver.get("https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&#jp/zh/")
        print(f"url=={url1}")
        driver.get(url1)
        time.sleep(1)
        selecet = driver.find_element(By.CLASS_NAME, "convert")
        Select(selecet).select_by_index(index)
        return driver

    def getTranslateData(self,input,index,  driver):
        try:
            if driver is None:
                driver = self.startFireFox(index)
            inputData = driver.find_element(By.ID, "inputText")
            inputData.clear()
            inputData.send_keys(input)
            btnTranslate = driver.find_element(By.CLASS_NAME, "blue-btn")
            btnTranslate.click()
            time.sleep(1)
            btnTranslate1 = driver.find_element(By.ID, "translateResult")
            data = btnTranslate1.__getattribute__("text")
            print(data)
            if data=="" or data is None:
                driver.refresh()
                time.sleep(3)
                selecet = driver.find_element(By.CLASS_NAME, "convert")
                Select(selecet).select_by_index(index)
                self.getTranslateData(input, index, driver)
            return data
        except Exception as e:
            driver.refresh()
            time.sleep(3)
            selecet = driver.find_element(By.CLASS_NAME, "convert")
            Select(selecet).select_by_index(index)
            self.getTranslateData(input, index, driver)
            print(e)

    pass
