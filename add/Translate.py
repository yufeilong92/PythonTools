import hashlib
import json
import time
from tkinter import Tk
from tkinter import  *

from Base.MainQuit import MainQuit

import requests
import langid

class Translate(MainQuit):
    def showDialog(self, mainRoot):
        root = Tk()
        root.title("保存数据到exle")
        root.config(bg="light gray")
        root.geometry("640x600")  # 设置窗口大小
        mFont = 10
        mSticky = W + E + S + N
        mWraplength = 300,
        mRlief = "groove"
        rowNum = 0
        showContext: Label
        Label(master=root, text="现有Excel:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                                  pady=4)
        selectExcelTV = Label(master=root, text="excel的地址", font=mFont,
                            wraplength=mWraplength, relief=mRlief)
        selectExcelTV.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Button(master=root, text="选择", font=mFont, relief=mRlief,
               command=lambda: self.adbSelectFileOne(selectExcelTV)).grid(row=rowNum, column=2, sticky=mSticky,
                                                                                      pady=4)
        len__ = root.children.__len__()
        for index in range(len__):
            root.columnconfigure(index, weight=1)

        rowNum += 1
        Label(master=root, text="保存列Two:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                              pady=4)
        createNameTwoEt = Entry(master=root, font=mFont)
        createNameTwoEt.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Button(master=root, text="翻译", font=mFont, relief=mRlief,
               command=lambda: self.translateApp(createNameTwoEt)).grid(row=rowNum, column=2, sticky=mSticky,
                                                                                      pady=4)
        self.registLisetener(root, mainRoot)
        mainloop()
        pass
    pass

    def translateApp(self, createNameTwoEt):
        datacontext=createNameTwoEt.get()
        print(f"========={datacontext}")

        def tran(api_id, key, word, from_lang, to_lang):
            # init salt and final_sign
            salt = str(time.time())[:10]
            final_sign = api_id + word + salt + key
            final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
            # 表单paramas
            paramas = {
                'q': word,
                'from': from_lang,
                'to': to_lang,
                'appid': '%s' % api_id,
                'salt': '%s' % salt,
                'sign': '%s' % final_sign
            }
            response = requests.get('http://api.fanyi.baidu.com/api/trans/vip/translate', params=paramas,
                                    timeout=10).content
            content = str(response, encoding="utf-8")
            json_reads = json.loads(content)
            try:
                return json_reads['trans_result'][0]['dst']
            # 百度翻译偶尔会拉闸
            except:
                print('    >正在尝试重新翻译...')
                return tran(api_id, key, word, from_lang, to_lang)

        api_id = '20180301000129461'
        key = 'Q8UqOZY4lFIr5z8LtROi'
        # word = '需要翻译的内容'
        from_lang = 'jp'  # 从：日文
        to_lang = 'zh'  # 翻译为：简体中文

        while True:
            word = input("输入你想翻译的内容: ")
            print(tran(api_id, key, word, from_lang, to_lang))

        pass