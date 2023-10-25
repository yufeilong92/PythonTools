#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 16:50
# @Author  : backpacker
# @File    : MainQuit.py
# @Description : $主窗口监听
from enum import Enum
from tkinter import  *

from  tkinter import  filedialog

from Base.FileDialogType import FileDialogType

from tkinter import  messagebox
class MainQuit:
    def registLisetener(self,root:Tk,mainRoot:Tk):
        root.protocol('WM_DELETE_WINDOW', lambda: self.QueryWindow(root, mainRoot))
    def QueryWindow(self,root,mainRoot):
        # 显示一个警告信息，点击确后，销毁窗口
        # if messagebox.showwarning("警告", "出现了一个错误"):
        # 这里必须使用 destory()关闭窗口
        root.destroy()
        mainRoot.deiconify()

    def selectFileDialog(self,tv:Label,type:FileDialogType,oldHint:str,newHint:str,isNew:bool):
        #选择目录
        path=None
        if type==FileDialogType.DIRECTORY:
            dialog=filedialog.askdirectory()
            if dialog is not None:
                path=dialog
        elif type==FileDialogType.DOCUMENT:#文件
            fileType=[("Xlsx",".xlsx")]
            dialog=filedialog.askopenfile(filetypes=fileType)
            if dialog is not  None:
                path=dialog.name

        if path is None or path=="":
           path=newHint if isNew else oldHint

        tv.config(text=path)


    def showWaring(self,message:str=None):
        messagebox.showwarning("温馨提示",message=message)
    def showAskQuestion(self,message:str=None):
        return  messagebox.askquestion("温馨提示",message=message)=="yes"

    def getLabelValue(self, tv: Label):
        return tv.cget("text")

    def getEntryValue(self,edt:Entry):
        return edt.get()

    def adbComboChange(self,*args):
        # print("adbComboChange ======")
        for item in args:
            if isinstance(item,StringVar):
                item.set("")
                # print("adbComboChange执行了=====")
        pass
