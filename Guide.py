#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/16 17:48
# @Author  : backpacker
# @File    : Guide.py
# @Description : $引导类
from tkinter import *

from ExportFile.ExportTxt import ExportTxt
from ExportFile.ExportXlsx import ExportXlsx
from ExportFile.MergeXlsx import MergeXlsx
from ExportFile.QueryRep import QueryRep
from Base.MainQuit import MainQuit
from Base.STARTGUI import STARTGUI
from FanTranslate.TranslateToolsWeb import TranslateToolsWeb

from add.addOneExcel import AddOneExecle
from colorSelect.ColorSelect import ColorSelect
from colorSelect.PictureReadTxt import PictureReadTxt


class Guide(MainQuit):
    def startGUI(self, root: Tk, type: STARTGUI):
        root.withdraw()
        if type == STARTGUI.COLORSELECT:  # 颜色选择器
            color = ColorSelect()
            color.showDialog(root)
        elif type == STARTGUI.EXPORTTXT:
            exportTxt = ExportTxt()
            exportTxt.showDialog(root)
        elif type == STARTGUI.EXPORTXLSX:
            exportxlsx = ExportXlsx()
            exportxlsx.showDialog(root)
        elif type == STARTGUI.QUERYREP:
            queryRep = QueryRep()
            queryRep.showDialog(root)
        elif type==STARTGUI.MERGE:
            merge=MergeXlsx()
            merge.showDialog(root)
        elif type==STARTGUI.PICTURETEXT:
            picture=PictureReadTxt()
            picture.showDialog(root)
        elif type==STARTGUI.ADDONEEXCEL:
            addoneExcel=AddOneExecle()
            addoneExcel.showDialog(root)
        elif type == STARTGUI.TRANSLATE:
            translate = TranslateToolsWeb()
            translate.showDialog(root)


    def guideTool(self):
        root = Tk()
        root.title("工具使用")
        root.geometry("640x540")  # 设置窗口大小
        root.config(bg="light gray")

        # mainQuitType=MainQuit()

        # mwith=15
        # mheight=1
        # mbg="#40E0D0"
        mFont = 8
        # =============第一行标题=================
        Button(master=root, text="颜色选择器", font=mFont,command=lambda: self.startGUI(root, STARTGUI.COLORSELECT)).grid(row=0, column=0, sticky=E + W)
        Button(master=root, text="导出TXT", font=mFont, command=lambda: self.startGUI(root, STARTGUI.EXPORTTXT)).grid(
            row=0, column=1, sticky=E + W)
        Button(master=root, text="导出XLSX", font=mFont, command=lambda: self.startGUI(root, STARTGUI.EXPORTXLSX)).grid(
            row=0, column=2, sticky=E + W)
        Button(master=root, text="查询重复", font=mFont, command=lambda: self.startGUI(root, STARTGUI.QUERYREP)).grid(
            row=0, column=3, sticky=E + W)
        Button(master=root, text="合并Xlsx", font=mFont, command=lambda: self.startGUI(root, STARTGUI.MERGE)).grid(
            row=0, column=4, sticky=E + W)

        # 给标题设置权重
        childrenLenght = root.children.__len__()
        for i in range(childrenLenght):
            root.columnconfigure(i, weight=1)
        Button(master=root, text="识别图片文字", font=mFont, command=lambda: self.startGUI(root, STARTGUI.PICTURETEXT)).grid(
            row=1, column=0, sticky=E + W)
        Button(master=root, text="添加数据到excel", font=mFont,
               command=lambda: self.startGUI(root, STARTGUI.ADDONEEXCEL)).grid(
            row=1, column=1, sticky=E + W)
        Button(master=root, text="翻译", font=mFont,
               command=lambda: self.startGUI(root, STARTGUI.TRANSLATE)).grid(
            row=1, column=2, sticky=E + W)
        # =============第二行开始=================
        # Button(master=root, text="颜色选择器",bg=mbg,font=mFont,command=lambda :adbColorSelect()).grid(row=1,column=0,sticky=E+W)
        # ==============================

        root.mainloop()
