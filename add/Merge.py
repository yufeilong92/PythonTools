import os
import subprocess
from datetime import datetime

from Base.FileDialogType import FileDialogType
from Base.MainQuit import MainQuit
from tkinter import Tk, filedialog

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
        Button(master=root, text="合成", font=mFont, relief=mRlief,
               command=lambda: self.mergefunction(selectTsFileTv, savceFileTsTV, editName, showContext)).grid(
            row=rowNum, column=0, columnspan=3,
            sticky=mSticky,
            pady=4)

        rowNum += 1
        showContext = Label(master=root, height=10, font=mFont, wraplength=600, bg="#5EA4DE")
        showContext.grid(row=rowNum, column=0, columnspan=3, sticky=mSticky, pady=4)

        self.registLisetener(root, mainRoot)
        mainloop()
        pass

    pass

    def mergefunction(self, selectTsFileTv, savceFileTsTV, editName, showContext):
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
        savetxt = f"{saveTsFile}/{name}.ts"
        pathlist = selectTsFile + "/*.ts"
        print(f"savetxt=={savetxt}")
        print(f"pathlist=={selectTsFile}")
        saveReplace = savetxt.replace("/", "\\")
        selectReplace = pathlist.replace("/", "\\")
        cmdd = f"copy /b {selectReplace}  {saveReplace}"
        os.system(f"start cmd.exe /k   {cmdd}")
        self.setTvContext(showContext, "========Success========\n   执行成功", TypeBgColor.Success)

        pass




