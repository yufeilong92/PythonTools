# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# from tkinter import Tk, Frame
# from tkinter import *
#
# from ExportFile.ExportXlsx import ExportXlsx
from Guide import Guide
# from Base.MainQuit import MainQuit, STARTGUI
# from colorSelect.ColorSelect import ColorSelect

# from ExportFile.ExportTxt import ExportTxt

# Press the green button in the gutter to run the script.
# def adbColorSelect(root):
#     root.withdraw()
#     selectColor= ColorSelect()
#     selectColor.showDialog(root)
#
#
# def adbExportTxT(root):
#     root.withdraw()
#     selectTxt=ExportTxt()
#     selectTxt.showDialog(root)
#     pass
#
#
# def adbExportXlsx(root):
#     root.withdraw()
#     selectXlsx=ExportXlsx()
#     selectXlsx.showDialog(root)
#
#     pass
#
#
# def adbQuesetRepetition(root):
#
#
#     pass


if __name__ == '__main__':
    guide=Guide()
    guide.guideTool()
    # print_hi('PyCharm')
    # root = Tk()
    # root.title("工具使用")
    # root.geometry("640x540")  # 设置窗口大小
    # root.config(bg="light gray")
    #
    # # mainQuitType=MainQuit()
    #
    # # mwith=15
    # # mheight=1
    # # mbg="#40E0D0"
    # mFont=8
    # # =============第一行标题=================
    # Button(master=root, text="颜色选择器",font=mFont,command=lambda :adbColorSelect(root)).grid(row=0,column=0,sticky=E+W)
    # Button(master=root, text="导出TXT",font=mFont,command=lambda :adbExportTxT(root)).grid(row=0,column=1,sticky=E+W)
    # Button(master=root, text="导出XLSX",font=mFont,command=lambda :adbExportXlsx(root)).grid(row=0,column=2,sticky=E+W)
    # Button(master=root, text="查询重复",font=mFont,command=lambda :adbQuesetRepetition(root)).grid(row=0,column=3,sticky=E+W)
    #
    # # Button(master=root, text="颜色选择器",font=mFont,command=lambda :mainQuitType.startGUI(root,STARTGUI.COLORSELECT)).grid(row=0,column=0,sticky=E+W)
    # # Button(master=root, text="导出TXT",font=mFont,command=lambda :mainQuitType.startGUI(root,STARTGUI.EXPORTTXT)).grid(row=0,column=1,sticky=E+W)
    # # Button(master=root, text="导出XLSX",font=mFont,command=lambda :mainQuitType.startGUI(root,STARTGUI.EXPORTXLSX)).grid(row=0,column=2,sticky=E+W)
    # # Button(master=root, text="查询重复",font=mFont,command=lambda :mainQuitType.startGUI(root,STARTGUI.QUERYREP)).grid(row=0,column=3,sticky=E+W)
    #
    #
    #
    # # 给标题设置权重
    # childrenLenght = root.children.__len__()
    # for i in range(childrenLenght):
    #     root.columnconfigure(i,weight=1)
    #
    # # =============第二行开始=================
    # # Button(master=root, text="颜色选择器",bg=mbg,font=mFont,command=lambda :adbColorSelect()).grid(row=1,column=0,sticky=E+W)
    # # ==============================
    #
    # root.mainloop()
