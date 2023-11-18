import hashlib
import json
import os
import random
import time
from tkinter import  *

from Base.MainQuit import MainQuit
from tkinter import filedialog
import requests
from tkinter import ttk
import tkinter as tk

from Base.TypeBgColor import TypeBgColor

from FanTranslate.old.BaiduPostTools import BaiduPostTools


class TranslateTools(MainQuit):
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
        Label(master=root, text="文件目录:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                                  pady=4)
        selectExcelTV = Label(master=root, text="", font=mFont,
                            wraplength=mWraplength, relief=mRlief)
        selectExcelTV.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Button(master=root, text="选择", font=mFont, relief=mRlief,
               command=lambda: self.adbSelectFileOne(selectExcelTV)).grid(row=rowNum, column=2, sticky=mSticky,
                                                                                      pady=4)
        len__ = root.children.__len__()
        for index in range(len__):
            root.columnconfigure(index, weight=1)

        rowNum += 1
        Label(master=root, text="选择翻译:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                              pady=4)
        combobox = ttk.Combobox(font=mFont, master=root,justify=tk.CENTER)
        combobox.grid(row=rowNum, column=1, sticky=mSticky, pady=4)
        combobox['values']=["日语--中文","英语--中文","中文--日语","中文--英语"]
        combobox['state']="readonly"
        combobox.current(0)
        Button(master=root, text="翻译", font=mFont, relief=mRlief,
               command=lambda: self.translateApp(combobox,selectExcelTV,showContext)).grid(row=rowNum, column=2, sticky=mSticky,
                                                                                      pady=4)

        rowNum += 1
        showContext = Label(master=root, height=10, font=mFont, wraplength=600, bg="#5EA4DE")
        showContext.grid(row=rowNum, column=0, columnspan=3, sticky=mSticky, pady=4)
        self.registLisetener(root, mainRoot)
        mainloop()
        pass

    def send_request(self,content,from_lang,to_lang,showContext:Label):
        salt = str(round(time.time() * 1000)) + str(random.randint(0, 9))
        data = "fanyideskweb" + content + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        sign = hashlib.md5()
        sign.update(data.encode("utf-8"))
        sign = sign.hexdigest()

        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1927650476@223.97.13.65;',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        }
        data = {
            'i': str(content),
            'from': f'{from_lang}',
            # 'from': 'ja',
            'to': f'{to_lang}',
            # 'to': 'zh-CHS',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': str(salt),
            'sign': str(sign),
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        try:
            res = requests.post(url=url, headers=headers, data=data)
            print(f"======={res.status_code}")
            print(f"====={res.json()}")
            htm=res.json()
            return htm['translateResult'][0][0]['tgt']
        except Exception as e:
            time.sleep(1)
            print(f"网络连接中{e}")
            self.setTvContext(showContext, "===========Error==========\n   网络重新连接", TypeBgColor.waring)
            self.send_request(content, from_lang, to_lang, showContext)
            pass

    def translateApp(self, combobox:COMMAND,selectExcelTV:Label,showContext:Label):
        selectPath = selectExcelTV.cget("text")
        if selectPath=="" or selectPath is None:
            self.setTvContext(showContext,"===========Error==========\n   请选项目录",TypeBgColor.waring)
            return
        listdir = os.listdir(selectPath)
        if listdir.__len__()==0:
            self.setTvContext(showContext, "===========Error==========\n   选择目录下没有文件", TypeBgColor.error)
            return
        selectTranslate = combobox.get()
        fromlang = 'ja'
        tolang = 'zh-CHS'
        if selectTranslate =="日语--中文":
            fromlang = 'ja'
            tolang = 'zh-CHS'
            pass
        elif selectTranslate=="英语--中文":
            fromlang = 'en'
            tolang = 'zh-CHS'
            pass
        elif selectTranslate =="中文--日语":
            fromlang = 'zh-CHS'
            tolang = 'ja'
            pass
        elif selectTranslate =="中文--英语":
            fromlang = 'zh-CHS'
            tolang = 'en'
            pass
        else:
            fromlang = 'ja'
            tolang = 'zh-CHS'
        for item in listdir:
            self.startTransta(selectPath,item,fromlang,tolang,showContext)
            time.sleep(6)
        pass
    def startTransta(self,selectPath:str,item:str,fromlang,tolang,showContext):
        split = item.split(".mp4")
        oldPath=selectPath+"/"+item
        content = split[0].strip()
        str1=' /.●~)(。…】【AQWERTYUIOPLKJHGFDSAZXCVBNM,.:`_=-+/;qwertyuiopasdfghjklzxcvbnm'
        table = str.maketrans('', '', str1)
        translate = content.translate(table)
        # content.replace("/","")
        # content.replace(".","")
        # content.replace("●","")
        # content.replace("~","")
        # content.replace(")","")
        # content.replace("(","")
        # content.replace("。","")

        print(f"翻译前的数据=={translate}")
        # tanslateall=Translator("zh","autodetect")
        # result=tanslateall.translate(translate)
        # print(result)
        # return

        baidu =BaiduPostTools()
        result = baidu.getTranslateRsult(translate)
        if result is None :
            time.sleep(10)
            result = baidu.getTranslateRsult(translate)
        if result is None:
            return
        print(f"翻译的结果=={result.strip()}")

        newPath=selectPath+"/"+result.strip()+".mp4"
        print(f"old={oldPath} \n========================\nnewpath={newPath}")
        try:
            if os.path.exists(oldPath) and not os.path.exists(newPath):
                print(f"不存在======================={newPath}")
                os.rename(oldPath, newPath)

        except Exception as e:
            print(f"抛出异常=={e}")
        self.setTvContext(showContext, f"===========Success==========\n  {oldPath}\n替换成{newPath}",
                          TypeBgColor.Success)
        pass
    def adbSelectFileOne(self, selectExcelTV):
        pathNum = filedialog.askdirectory()
        if pathNum =="" or pathNum is None:
            return
        selectExcelTV.config(text=f"{pathNum}")
        pass

    def tran(self,api_id, key, word, from_lang, to_lang):
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
            return self.tran(api_id, key, word, from_lang, to_lang)


    def baiduTranslate(self,contenxt):
        api_id = '20180301000129461'
        key = 'Q8UqOZY4lFIr5z8LtROi'
        # word = '需要翻译的内容'
        from_lang = 'jp'  # 从：日文
        to_lang = 'zh'  # 翻译为：简体中文
        return self.tran(api_id, key, contenxt, from_lang, to_lang)