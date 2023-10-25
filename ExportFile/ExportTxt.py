#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/15 16:12
# @Author  : backpacker
# @File    : ExportTxt.py
# @Description : $保存目录导出TXT 文件
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import  os
from Base.MainQuit import MainQuit

class ExportTxt(MainQuit):
    def adbSaveText(self,selectBtn, saveBtn, saveName):
        saveName = saveName.get()
        selectFilePath = selectBtn.cget("text")
        saveFilePath = saveBtn.cget("text")
        print(f"selectFilePath{saveFilePath}")
        if selectFilePath == "导出的目录":
            messagebox.showwarning("温馨提示", "请选择导出目录")
            return
        print(f"savefilepath{saveFilePath}")
        if saveFilePath == "保存的目录":
            messagebox.showwarning("温馨提示", "请选择保存的目录")
            return
        print(f"savename{saveName}")
        if saveName is None or saveName == "":
            messagebox.showwarning("温馨提示", "请输入保存名称")
            return

        showinfo = messagebox.askquestion(title="温馨提示", message="是否确认保存")
        if showinfo != "yes":
            print("退出")
            return

        print("保存")
        listdir = os.listdir(selectFilePath)
        if listdir.__len__() == 0:
            messagebox.showwarning("温馨提示","选择目录下没有内容")
            return
        saveOverPath=saveFilePath+"/"+saveName+".txt"
        if os.path.exists(saveOverPath):#判断是否存在
            if messagebox.askquestion("温馨提示", message="文件已经存在是否追加,不追加则覆盖") == "yes":
                #追加
                self.writeData(saveOverPath, listdir=listdir,method="a")
            else:#覆盖
                os.remove(saveOverPath)
                self.writeData(saveOverPath, listdir=listdir,method="w")
        else:
            self.writeData(saveOverPath, listdir=listdir,method="w")

        if messagebox.askquestion("温馨提示", message="保存成功,是否打开对应目录") == "yes":
            os.startfile(saveFilePath)


    def writeData(self,saveOverPath,listdir,method:str):
        file = open(saveOverPath, method,encoding="utf-8")
        for item in listdir:
            file.write(item)
            file.write("\n")
        file.close()
        pass
    def selectFile(self, txt: Label, isave):
        fileName = filedialog.askdirectory()
        print(f"{fileName}")
        if fileName is None or fileName == "":
            if isave:
                fileName = "保存的目录"
            else:
                fileName = "导出的目录"

        txt.config(text=fileName)

    def showDialog(self,mainRoot:Tk):
        root = Tk()

        root.config(bg="light gray")
        root.geometry("640x540")#设置窗口大小
        root.title("导出TXT")

        mfont = 10
        mWraplength=300,
        # ===========================
        Label(master=root, text="地址 :", font=mfont).grid(row=0, column=0, sticky=N + S + W + E, pady=4)
        selectBtn = Label(master=root, text="导出的目录", wraplength=mWraplength, justify=LEFT, font=mfont)
        selectBtn.grid(row=0, column=1, sticky=N + S + W + E, pady=4)
        Button(master=root, text="选择", font=mfont, command=lambda: self.selectFile(selectBtn, False)).grid(row=0,
                                                                                                             column=2,
                                                                                                             sticky=N + S + W + E,
                                                                                                             pady=4)
        len__ = root.children.__len__()

        for i in range(len__):
            root.columnconfigure(i, weight=1)

        Label(master=root, text="地址 :", font=mfont).grid(row=1, column=0, sticky=N + S + W + E, pady=4)

        saveBtn = Label(master=root, text="保存的目录",  wraplength=mWraplength,justify=LEFT, font=mfont)
        saveBtn.grid(row=1, column=1, sticky=N + S + W + E, pady=4)
        Button(master=root, text="选择", font=mfont, command=lambda: self.selectFile(saveBtn, True)).grid(row=1,
                                                                                                          column=2,
                                                                                                          sticky=N + S + W + E,
                                                                                                          pady=4)

        Label(master=root, text="文本名称 :", font=mfont).grid(row=2, column=0, sticky=N + S + W + E, pady=4)

        saveName = Entry(master=root,font=mfont)
        saveName.grid(row=2, column=1, sticky=N + S + W + E, pady=4)
        Label(master=root, text=".txt", font=mfont).grid(row=2, column=2, sticky=N + S + W + E, pady=4)

        Button(master=root, text="保存", font=mfont, command=lambda:self.adbSaveText(selectBtn, saveBtn, saveName)) \
            .grid(row=3, column=1, sticky=N + S + W + E, pady=8)



        # 使用协议机制与窗口交互，并回调用户自定义的函数
        super().registLisetener(root,mainRoot)
        # root.protocol('WM_DELETE_WINDOW', lambda :self.QueryWindow(root,mainRoot))
        mainloop()

    pass


    # def QueryWindow(self,root,mainRoot):
    #     # 显示一个警告信息，点击确后，销毁窗口
    #     # if messagebox.showwarning("警告", "出现了一个错误"):
    #     # 这里必须使用 destory()关闭窗口
    #     root.destroy()
    #     mainRoot.deiconify()

