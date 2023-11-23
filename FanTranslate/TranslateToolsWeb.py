import hashlib
import json
import os
import random
import re
import time
from tkinter import *


from Base.FileDialogType import FileDialogType
from Base.MainQuit import MainQuit
from tkinter import filedialog
import requests
from tkinter import ttk
import tkinter as tk
import sys

sys.stdout = sys.stdout
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
               command=lambda: self.adbSelectFileOne(selectExcelTV, showContext)).grid(row=rowNum, column=2,
                                                                                       sticky=mSticky,
                                                                                       pady=4)
        len__ = root.children.__len__()
        for index in range(len__):
            root.columnconfigure(index, weight=1)
        rowNum += 1
        Label(master=root, text="是否保存日志:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                                 pady=4)
        comboboxSavelog = ttk.Combobox(font=mFont, master=root, justify=tk.CENTER)
        comboboxSavelog.grid(row=rowNum, column=1, columnspan=2, sticky=mSticky, pady=4)
        comboboxSavelog['values'] = ["是", "否"]
        comboboxSavelog['state'] = "readonly"
        comboboxSavelog.config(font=mFont)
        comboboxSavelog.current(1)

        rowNum += 1
        Label(master=root, text="LOG目录:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                            pady=4)
        logPathTv = Label(master=root, text="", font=mFont, relief=mRlief)
        logPathTv.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        (Button(master=root, text="选择", font=mFont, relief=mRlief,
                command=lambda: self.selectFileDialog(logPathTv, FileDialogType.DIRECTORY, "", "", False)).grid(
            row=rowNum, column=2, sticky=mSticky, pady=4))

        rowNum += 1
        Label(master=root, text="LOG名称：", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                            pady=4)
        edit = Entry(master=root, font=mFont, relief=mRlief)
        edit.grid(row=rowNum, column=1, columnspan=2, sticky=mSticky, pady=4)

        rowNum += 1
        Label(master=root, text="选择翻译:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                             pady=4)
        combobox = ttk.Combobox(font=mFont, master=root, justify=tk.CENTER)
        combobox.grid(row=rowNum, column=1, sticky=mSticky, pady=4)
        combobox['values'] = ["日语--中文", "英语--中文", "中文--日语", "中文--英语","自动检测"]
        combobox['state'] = "readonly"
        combobox.config(font=mFont)
        combobox.current(0)
        Button(master=root, text="翻译", font=mFont, relief=mRlief,
               command=lambda: self.translateApp(combobox, selectExcelTV, showContext, comboboxSavelog, logPathTv,
                                                 edit)).grid(row=rowNum, column=2, sticky=mSticky,
                                                             pady=4)

        rowNum += 1
        showContext = Label(master=root, height=10, font=mFont, wraplength=600, bg="#5EA4DE")
        showContext.grid(row=rowNum, column=0, columnspan=3, sticky=mSticky, pady=4)
        self.registLisetener(root, mainRoot)
        mainloop()
        pass

    def translateApp(self, combobox: COMMAND, selectExcelTV: Label, showContext: Label, comboboxSavelog, logPathTv,
                     edit):
        # 判断是否要保存日志
        savelog = comboboxSavelog.get()
        isSaveLog = False
        f = None
        pathlog=""
        print(f"savelog==={savelog}")
        if savelog == "是":
            path = logPathTv.cget("text")
            if path == "" or path is None:
                self.setTvContext(showContext, "请选择log保存目录", TypeBgColor.waring)
                return
            name = edit.get()
            if name == "" or name is None:
                self.setTvContext(showContext, "请输入log的名称", TypeBgColor.waring)
                return
            isSaveLog = True
            pathlog=f"{path}/{name}.txt"
        else:
            isSaveLog = False
            f = None
        self.setTvContext(showContext, "", TypeBgColor.defend)
        selectPath = selectExcelTV.cget("text")
        if selectPath == "" or selectPath is None:
            self.setTvContext(showContext, "===========Error==========\n   请选项目录", TypeBgColor.waring)
            return
        listdir = os.listdir(selectPath)
        if listdir.__len__() == 0:
            self.setTvContext(showContext, "===========Error==========\n   选择目录下没有文件", TypeBgColor.error)
            return
        selectTranslate = combobox.get()
        fromlang = 'jp'
        tolang = 'zh'
        if selectTranslate == "日语--中文":
            fromlang = 'jp'
            tolang = 'zh'
            pass
        elif selectTranslate == "英语--中文":
            fromlang = 'en'
            tolang = 'zh'
            pass
        elif selectTranslate == "中文--日语":
            fromlang = 'zh'
            tolang = 'jp'
            pass
        elif selectTranslate == "中文--英语":
            fromlang = 'zh'
            tolang = 'en'
            pass
        elif selectTranslate=="自动检测":
            fromlang = 'auto'
            tolang = 'zh'
        else:
            fromlang = 'ja'
            tolang = 'zh-CHS'
        startWebBaidu = StartBaiduWebTest()
        print(f"{selectTranslate}=={fromlang}=={tolang}")
        driver = startWebBaidu.startFireFox(fromlang,tolang)
        time.sleep(4)
        for item in listdir:
            self.startTransta(selectPath, item, fromlang, tolang, showContext, startWebBaidu, driver, isSaveLog, pathlog)
            time.sleep(1)
        pass

    def startTransta(self, selectPath, item, fromlang, tolang, showContext, startWebBaidu, driver, isSaveLog, pathlog):
        if item.find(".mp4")!=-1:
            split = item.split(".mp4")
            translate = split[0].strip()
        elif item.find(".ts")!=-1:
            split = item.split(".ts")
            translate = split[0].strip()
        elif item.find(".txt")!=-1:
            split = item.split(".txt")
            translate = split[0].strip()
        else:
            translate=item
        # print(f"原文件=={item}\n.mp4=={find}over\n")
        # find = item.find(".ts")
        # print(f"原文件=={item}\n.ts=={find}over\n")
        # find = item.find(".txt")
        # print(f"原文件=={item}\n.txt=={find}over\n")

        oldPath = selectPath + "/" + item

        # str1=' /.●~)(。…】【AQWERTYUIOPLKJHGFDSAZXCVBNM,.:`_=-+/;qwertyuiopasdfghjklzxcvbnm'
        # str1=' /.●~)(。…】【,.:`_=-+/;'
        # table = str.maketrans('', '', str1)
        # translate = content.translate(table)
        # content.replace("/","")
        # content.replace(".","")
        # content.replace("●","")
        # content.replace("~","")
        # content.replace(")","")
        # content.replace("(","")
        # content.replace("。","")
        translate = self.mattchData(translate)
        if isSaveLog and pathlog !="" :
            self.saveLog(pathlog,f"翻译前的数据=={translate}")
        print(f"翻译前的数据=={translate}\n",f"翻译前的数据=={translate}\n")
        # tanslateall=Translator("zh","autodetect")
        # result=tanslateall.translate(translate)
        # print(result)
        # return
        if translate == "" or translate is None:
            return

        result = startWebBaidu.getTranslateData(translate,fromlang,tolang, driver)
        if result is None:
            time.sleep(1)
            driver.refresh()
            time.sleep(5)
            result = startWebBaidu.getTranslateData(translate,fromlang,tolang, driver)
        if result is None:
            return

        if isSaveLog and pathlog !="":
            self.saveLog(pathlog, f"翻译的结果=={result}")
        print(f"翻译的结果=={result}\n")
        newPath = selectPath + "/" + result.strip() + ".mp4"
        # print(f"old={oldPath} \n=====\nnewpath={newPath}")
        try:

            if not os.path.exists(newPath) and os.path.exists(oldPath):
                if isSaveLog and pathlog !="":
                    self.saveLog(pathlog, f"====不存在{newPath}===")
                print(f"====不存在{newPath}===\n")
                os.rename(oldPath, newPath)
            else:
                if isSaveLog and pathlog !="":
                    self.saveLog(pathlog, f"<<<{newPath}存在>>>")
                print(f"<<<{newPath}存在>>>\n")
                # self.setTvContext(showContext, f"===========wring==========\n   {newPath}文件已经存在", TypeBgColor.waring)
                return
        except Exception as e:
            if isSaveLog and pathlog !="":
                self.saveLog(pathlog, f"抛出异常=={e}")
            print(f"抛出异常=={e}\n")
        self.setTvContext(showContext, f"===========Success==========\n  {oldPath}\n替换成{newPath}\n",TypeBgColor.Success)
        pass

    def adbSelectFileOne(self, selectExcelTV, showcontxt):
        self.setTvContext(showcontxt, "", TypeBgColor.defend)
        pathNum = filedialog.askdirectory()
        if pathNum == "" or pathNum is None:
            return
        selectExcelTV.config(text=f"{pathNum}")
        pass
