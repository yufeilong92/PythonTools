import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
if __name__=="__main__":
    driver = webdriver.Firefox()
    # url = "https://www.iciba.com/translate"
    # url = "https://fanyi.youdao.com/index.html#/?keyfrom=cidian"
    url = "https://m.youdao.com/translate"
    # url = "https://fanyi.youdao.com/index.html#/"
    driver.get(url)
    driver.refresh()

    selecet = driver.find_element(By.CLASS_NAME, "convert")
    # selecet.text="日译中"
    Select(selecet).select_by_index(8)

    inputData = driver.find_element(By.ID,"inputText")
    inputData.send_keys("你好")

    btnTranslate = driver.find_element(By.CLASS_NAME, "blue-btn")
    btnTranslate.click()
    time.sleep(2)
    btnTranslate1 = driver.find_element(By.ID, "translateResult")
    getattribute__ = btnTranslate1.__getattribute__("text")
    print(getattribute__)
    pass