#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/13 13:37
# @Author  : backpacker
# @File    : PictureReadTxt.py
# @Description : $
from tkinter import *

import pytesseract

from Base.MainQuit import MainQuit
from tkinter import  filedialog

from PIL import Image
import cv2

class PictureReadTxt(MainQuit):

    def showDialog(self,mainRoot):
        root = Tk()
        root.title("查重工具")
        root.config(bg="light gray")
        root.geometry("640x540")  # 设置窗口大小
        mFont = 10
        mSticky = W + E + S + N
        mWraplength = 300,
        mRlief = "groove"
        Label(master=root, text="原文件One：", font=mFont, relief=mRlief).grid(row=0, column=0, sticky=mSticky,
                                                                              pady=4)
        pictureTv = Label(master=root, text="图片地址", font=mFont,wraplength=mWraplength, relief=mRlief)
        pictureTv.grid(row=0, column=1, sticky=mSticky,
                   pady=4)
        Button(master=root, text="选择", font=mFont, relief=mRlief,command=lambda :self.adbSelectPicture(pictureTv)).grid(row=0, column=2, sticky=mSticky,
                                                                              pady=4)

        len__ = root.children.__len__()

        for index in range(len__):
            root.columnconfigure(weight=1,index=index)
        # +=============================================

        showContexttv = Text(master=root, height=100, font=mFont,exportselection=True)

        Button(master=root, text="识别", font=mFont,
               command=lambda: self.adbReadPictureTxt(pictureTv,showContexttv)).grid(row=1, column=1, sticky=mSticky,
                                                               pady=4)
        showContexttv.grid(row=2, column=0, rowspan=3,columnspan=3, sticky=mSticky,
                          pady=4)


        self.registLisetener(root,mainRoot)
        mainloop()


        pass

    def adbSelectPicture(self, pictureTv:Label):
        typeatts={("PNG",".png"),("JPG",".jpg")}
        picturePath = filedialog.askopenfilename(filetypes=typeatts)
        oldpatch = pictureTv.cget("text")
        if oldpatch==picturePath:
            return
        if picturePath is None or picturePath == "":
            pictureTv.config(text="图片地址")
        else:
            pictureTv.config(text=picturePath)
        pass

    def adbReadPictureTxt(self, pictureTv,tv:Text):
        path = pictureTv.cget("text")
        if path==None or path=="图片地址":
            self.showWaring("请选择识别图片")
            return
        # imread = cv2.imread(path)
        print(path)
        image_open = Image.open(path)
        string = pytesseract.image_to_string(image_open)
        cget = tv.get(0.0,"end")
        tv.insert("end",f"{cget}{''}")
        tv.update()

        pass
