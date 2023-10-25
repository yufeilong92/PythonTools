#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 23:02
# @Author  : backpacker
# @File    : addOneExcel.py
# @Description : $
import os
from tkinter import Tk, filedialog, messagebox
from tkinter import *

from openpyxl import Workbook ,load_workbook
from openpyxl.worksheet.worksheet import Worksheet

from Base.FileDialogType import FileDialogType
from Base.MainQuit import MainQuit


class AddOneExecle(MainQuit):

    def adbSelectFileOne(self, selectPathTv):
        type = {("XLSX", ".xlsx")}
        selectOnePath = filedialog.askopenfilename(filetypes=type)
        oldPath = selectPathTv.cget("text")
        if oldPath == selectOnePath:
            return
        if selectOnePath is None or selectOnePath == "":
            selectPathTv.config(text="excel的地址")
            return
        print(f"{selectOnePath}")
        selectPathTv.config(text=selectOnePath)

        pass

    def showDialog(self, mainRoot):
        root = Tk()
        root.title("保存数据到exle")
        root.config(bg="light gray")
        root.geometry("640x540")  # 设置窗口大小
        mFont = 10
        mSticky = W + E + S + N
        mWraplength = 300,
        mRlief = "groove"
        rowNum=0
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
        # ===============标题权重===================
        rowNum += 1
        Label(master=root, text="创建新的:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                              pady=4)
        createExcelFileTV = Label(master=root, text="excel的目录", font=mFont,
                              wraplength=mWraplength, relief=mRlief)
        createExcelFileTV.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Button(master=root, text="选择", font=mFont, relief=mRlief,
               command=lambda: self.selectFileDialog(createExcelFileTV,FileDialogType.DIRECTORY,"excel的目录", "",
                                                     False)).grid(row=rowNum, column=2, sticky=mSticky,
                                                                          pady=4)
        rowNum += 1
        Label(master=root, text="新的名称:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                             pady=4)
        createNameEt = Entry(master=root, text="请输入名称", font=mFont)
        createNameEt.grid(row=rowNum, column=1, sticky=mSticky, pady=4)

        Label(master=root, text=".xlsx", font=mFont, relief=mRlief).grid(row=rowNum, column=2, sticky=mSticky,

                                                                          pady=4)
        rowNum += 1
        Label(master=root, text="保存列One:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky, pady=4)
        createNameOneEt = Entry(master=root,  font=mFont)
        createNameOneEt.grid(row=rowNum, column=1,columnspan=2, sticky=mSticky, pady=4)


        rowNum += 1
        Label(master=root, text="保存列Two:", font=mFont, relief=mRlief).grid(row=rowNum, column=0, sticky=mSticky,
                                                                             pady=4)
        createNameTwoEt=Entry(master=root,font=mFont)
        createNameTwoEt.grid(row=rowNum, column=1,columnspan=2, sticky=mSticky, pady=4)


        rowNum += 1
        Button(master=root, text="清空列One和Two", font=mFont, relief=mRlief,
               command=lambda: self.clearOneTwo(createNameOneEt,createNameTwoEt)).grid(row=rowNum, column=0,columnspan=3, sticky=mSticky,
                                                                  pady=4)

        rowNum += 1
        Button(master=root, text="添加", font=mFont, relief=mRlief,
               command=lambda: self.addSaveExcle(selectExcelTV,createExcelFileTV,createNameEt,createNameOneEt,createNameTwoEt)).grid(row=rowNum, column=0,columnspan=3, sticky=mSticky,
                                                                  pady=4)
        rowNum += 1
        Label(master=root,text="提示：默认优选添加到现有excele,默认表一,,其次是新建excele",font=mFont).grid(row=rowNum,column=0,columnspan=3,sticky=mSticky,pady=4)



        self.registLisetener(root, mainRoot)
        mainloop()
        pass

    pass



    def clearOneTwo(self, createNameOneEt, createNameTwoEt):
        createNameTwoEt.delete(0,"end")
        createNameOneEt.delete(0,"end")
        pass
    #selectExcelTV 现有的excel
    #createExcelFileTV 创建的excle目录
    #createNameEt 创建的名称
    #createNameOneEt one 数据
    #createNameTwoEt two 数据
    def addSaveExcle(self, selectExcelTV, createExcelFileTV, createNameEt, createNameOneEt, createNameTwoEt):
        #现有的数据

        try:
            selecetExcele = selectExcelTV.cget("text")
            createPath = createExcelFileTV.cget("text")
            createSheetName = createNameEt.get()
            savePath=None
            wb:Workbook=None
            sh:Worksheet=None
            isrep=False;
            if selecetExcele!="excel的地址":
                savePath=selecetExcele
                wb=load_workbook(selecetExcele)
                mOnesheetnames = wb.sheetnames
                print(f"{mOnesheetnames}")
                sheetOne = mOnesheetnames[0]
                sh = wb[sheetOne]
                print(f"{mOnesheetnames}//{sh}//{sh.max_row}")
                rowsOne = sh.max_row+1

                isrep=True
                pass
            else:
            #创建新表添加数据
                savePath=createPath+"/"+createSheetName+".xlsx"
                if os.path.exists(savePath):
                    messagebox.showwarning("温馨提示",f"{savePath},文件已经存在")
                    return

                wb = Workbook()
                sh = wb.create_sheet(createSheetName,0)
                rowsOne=1
                isrep = True
                pass
            oneData = createNameOneEt.get()
            if oneData is None or oneData =="":
                messagebox.showwarning("温馨提示","列One 数据为空")
                return
            twoData = createNameTwoEt.get()
            if twoData is None or twoData=="":
                messagebox.showwarning("温馨提示", "列Two 数据为空")
                return
           #=========判断是否重复============
            if isrep:
                sh_rows = sh.rows
                #maxcolumn = sh.max_column#列
                #maxrow = sh.max_row #行
                #第一列数据
                oneSheetData = sh.iter_cols(1, 1, values_only=True)
                mOneList=[]
                for item in oneSheetData:
                    if item is not  None:
                        for itemA in item:
                            if itemA is not  None:
                                mOneList.append(itemA)
                print(f"oneList=={mOneList}")
                if mOneList.__len__()!=0 :
                    if oneData in mOneList:
                        messagebox.showwarning("温馨提示",f"数据One{oneData}数据重复")
                        return

                # 第一列数据
                twoSheetData = sh.iter_cols(2, 2, values_only=True)
                mTwoList = []
                for item in twoSheetData:
                    if item is not None:
                        for itemA in item:
                            if itemA is not None:
                                mTwoList.append(itemA)
                print(f"twoList=={mTwoList}")
                if mTwoList.__len__()!=0:
                    if twoData in mTwoList:
                        messagebox.showwarning("温馨提示", f"数据Two{twoData}数据重复")
                        return
                        #=============保存=============
            sh.cell(row=rowsOne , column=1).value = f"{oneData}"
            sh.cell(row=rowsOne , column=2).value = f"{twoData}"

            wb.save(savePath)
            wb.close()
            messagebox.showinfo("温馨提示", f"要保存的文件{savePath}成功")
        except:
            messagebox.showerror("温馨提示", f"要保存的文件{savePath}正在打开，或者异常，请关闭重试")


            pass
