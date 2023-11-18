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
from FanTranslate.StartBaiduWebTest import StartBaiduWebTest


class TranslateToolsWeb(MainQuit):
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
        startWebBaidu=StartBaiduWebTest()
        driver = startWebBaidu.startFireFox()
        time.sleep(4)
        for item in listdir:
            self.startTransta(selectPath,item,fromlang,tolang,showContext,startWebBaidu,driver)
            time.sleep(1)
        pass
    def startTransta(self,selectPath:str,item:str,fromlang,tolang,showContext,startWebBaidu,driver):
        split = item.split(".mp4")
        oldPath = selectPath + "/" + item

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

        print(f"翻译前的数据=={translate}\n")
        # tanslateall=Translator("zh","autodetect")
        # result=tanslateall.translate(translate)
        # print(result)
        # return
        result = startWebBaidu.getTranslateData(translate, driver)
        if result is None:
            time.sleep(1)
            driver.refresh()
            result = startWebBaidu.getTranslateData(translate, driver)
        if result is None:
            return
        print(f"翻译的结果=={result}\n")
        newPath=selectPath+"/"+result.strip()+".mp4"
        # print(f"old={oldPath} \n=====\nnewpath={newPath}")
        try:

            if not os.path.exists(newPath) and os.path.exists(oldPath) :
                print(f"====不存在{newPath}===\n")
                os.rename(oldPath, newPath)
            else:
                print(f"<<<{newPath}存在>>>\n")
                # self.setTvContext(showContext, f"===========wring==========\n   {newPath}文件已经存在", TypeBgColor.waring)
                return
        except Exception as e:
            print(f"抛出异常=={e}\n")
        self.setTvContext(showContext, f"===========Success==========\n  {oldPath}\n替换成{newPath}\n"
                                       f""
                                       f"",
                          TypeBgColor.Success)
        pass
    def adbSelectFileOne(self, selectExcelTV):
        pathNum = filedialog.askdirectory()
        if pathNum =="" or pathNum is None:
            return
        selectExcelTV.config(text=f"{pathNum}")
        pass




