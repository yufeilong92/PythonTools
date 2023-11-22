import os
import subprocess
from datetime import datetime

from Base.FileDialogType import FileDialogType
from Base.MainQuit import MainQuit
from tkinter import Tk, filedialog, ttk
import tkinter as tk
from tkinter import *

from Base.TypeBgColor import TypeBgColor


class Merge(MainQuit):
    def selectFileDialogs(self,tv:Label,type:FileDialogType,showContext):
        self.setTvContext(showContext,"",TypeBgColor.defend)
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
        tv.config(text=path)
    def showDialog(self, mainRoot):
        root = Tk()
        root.title("合成ts文件")
        root.geometry("640x600")
        root.config(bg="light gray")
        mFont = 10
        mSticky = W + E + S + N
        mWraplength = 300,
        mRlief = "groove"
        rowNum = 0
        showContext: Label
        Label(master=root, text="文件目录:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                             pady=4)
        selectTsFileTv = Label(master=root, text="", font=mFont,
                               wraplength=mWraplength, relief=mRlief)
        selectTsFileTv.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Button(master=root, text="选择", font=mFont, relief=mRlief,
               command=lambda: self.selectFileDialogs(selectTsFileTv, FileDialogType.DIRECTORY, showContext)).grid(
            row=rowNum, column=2,
            sticky=mSticky,
            pady=4)
        childLength = root.children.__len__()

        for index in range(childLength):
            root.columnconfigure(index, weight=1)

        rowNum += 1
        Label(master=root, text="保存目录:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                             pady=4)
        savceFileTsTV = Label(master=root, text="", font=mFont,
                              wraplength=mWraplength, relief=mRlief)
        savceFileTsTV.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Button(master=root, text="选择", font=mFont, relief=mRlief,
               command=lambda: self.selectFileDialogs(savceFileTsTV, FileDialogType.DIRECTORY, showContext)).grid(
            row=rowNum, column=2,
            sticky=mSticky,
            pady=4)

        rowNum += 1
        Label(master=root, text="保存文件名称:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                                 pady=4)
        editName = Entry(master=root, font=mFont, relief=mRlief)
        editName.grid(row=rowNum, column=1, columnspan=2, sticky=mSticky, pady=4)

        rowNum += 1
        Label(master=root, text="保存格式:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                             pady=4)
        comboboxCopySaveType = ttk.Combobox(font=mFont, master=root, justify=tk.CENTER)
        comboboxCopySaveType.grid(row=rowNum, column=1, sticky=mSticky, pady=4)
        comboboxCopySaveType['values'] = ["TS", "MP4"]
        comboboxCopySaveType['state'] = "readonly"
        comboboxCopySaveType.config(font=mFont)
        comboboxCopySaveType.current(0)
        Button(master=root, text="copy /b 合成", font=mFont, relief=mRlief,
               command=lambda: self.mergefunction(selectTsFileTv, savceFileTsTV, editName, comboboxCopySaveType,showContext)).grid(
            row=rowNum, column=2,
            sticky=mSticky,
            pady=4)
        rowNum += 1
        Label(master=root, text="保存格式:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                                 pady=4)
        comboboxSaveType = ttk.Combobox(font=mFont, master=root, justify=tk.CENTER)
        comboboxSaveType.grid(row=rowNum, column=1, sticky=mSticky, pady=4)
        comboboxSaveType['values'] = ["TS", "MP4"]
        comboboxSaveType['state'] = "readonly"
        comboboxCopySaveType.config(font=mFont)
        comboboxSaveType.current(0)
        Button(master=root, text="ffmpeg  合成", font=mFont, relief=mRlief,
               command=lambda: self.mergefunctionffmpeg(selectTsFileTv, savceFileTsTV, editName, comboboxSaveType,showContext)).grid(
            row=rowNum, column=2, sticky=mSticky,
            pady=4)
        rowNum += 1
        showContext = Label(master=root, height=10, font=mFont, wraplength=600, bg="#5EA4DE")
        showContext.grid(row=rowNum, column=0, columnspan=3, sticky=mSticky, pady=4)

        self.registLisetener(root, mainRoot)
        mainloop()
        pass

    pass

    def mergefunction(self, selectTsFileTv, savceFileTsTV, editName, comboboxCopySaveType,showContext):
        selectTsFile = selectTsFileTv.cget("text")
        if selectTsFile == "" or savceFileTsTV is None:
            self.setTvContext(showContext, "========Waring========\n   请选择文件目录", TypeBgColor.waring)
            return

        saveTsFile = savceFileTsTV.cget("text")
        if saveTsFile == "" or saveTsFile is None:
            self.setTvContext(showContext, "========Waring========\n   请选择保存文件目录", TypeBgColor.waring)
            return
        name = editName.get()
        if name == "" or name is None:
            self.setTvContext(showContext, "========Waring========\n   请输入保持的名称", TypeBgColor.waring)
            return
        savetype = comboboxCopySaveType.get()
        savetxt = f"{saveTsFile}/{name}.{savetype.lower()}"
        pathlist = selectTsFile + "/*.ts"
        print(f"savetxt=={savetxt}")
        print(f"pathlist=={selectTsFile}")
        saveReplace = savetxt.replace("/", "\\")
        selectReplace = pathlist.replace("/", "\\")
        cmdd = f"copy /b {selectReplace}  {saveReplace}"
        os.system(f"start cmd.exe /k   {cmdd}")
        self.setTvContext(showContext, "========Success========\n   执行成功", TypeBgColor.Success)

        pass

    def mergefunctionffmpeg(self, selectTsFileTv, savceFileTsTV, editName, comboboxSaveType,showContext):
        selectTsFile = selectTsFileTv.cget("text")
        if selectTsFile == "" or savceFileTsTV is None:
            self.setTvContext(showContext, "========Waring========\n   请选择文件目录", TypeBgColor.waring)
            return

        saveTsFile = savceFileTsTV.cget("text")
        if saveTsFile == "" or saveTsFile is None:
            self.setTvContext(showContext, "========Waring========\n   请选择保存文件目录", TypeBgColor.waring)
            return
        name = editName.get()
        if name == "" or name is None:
            self.setTvContext(showContext, "========Waring========\n   请输入保持的名称", TypeBgColor.waring)
            return

        selectPath = os.listdir(selectTsFile)
        len__ = selectPath.__len__()
        if len__==0:
            self.setTvContext(showContext,"========Waring========\n   选择的目录下没有ts文件", TypeBgColor.waring)
            return
        selectPath.sort()
        # start = datetime.now()
        # print('开始合成，初始时间为:', datetime.now())
        savetype = comboboxSaveType.get()
        pathlist = saveTsFile + f"/{name}.{savetype.lower()}"
        fileStr = "concat:"
        for index in range(len__):
            print(f"index=={index}")
            if index == len__ - 1:
                fileStr += f"{selectTsFile}/{selectPath[index]}"
            else:
                fileStr += f"{selectTsFile}/{selectPath[index]}|"

        # cmdd = f"ffmpeg -i "concat:1.ts|2.ts" -c copy output.mp4"
        cmdd = f"ffmpeg -i \"{fileStr}\" -c copy {pathlist}"
        os.system(f"start cmd.exe /k   {cmdd}")
        # print('合成后的当前时间为：', datetime.now())
        # print('合成视频完成！用时：' + str(datetime.now() - start))
        self.setTvContext(showContext, "========Success========\n   执行成功", TypeBgColor.Success)
        pass

        pass



