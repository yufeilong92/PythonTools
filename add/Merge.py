import os
import subprocess
from datetime import datetime

from Base.FileDialogType import FileDialogType
from Base.MainQuit import MainQuit
from tkinter import Tk

from tkinter import *

from Base.TypeBgColor import TypeBgColor


class Merge(MainQuit):
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
               command=lambda: self.selectFileDialog(selectTsFileTv, FileDialogType.DIRECTORY, "", "", False)).grid(
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
               command=lambda: self.selectFileDialog(savceFileTsTV, FileDialogType.DIRECTORY, "", "", False)).grid(
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
        self.test(selectTsFile, saveTsFile, name)
        self.setTvContext(showContext, "========Success========\n   执行成功", TypeBgColor.Success)

        pass

    def test(self, path, save_path, name):
        file_names = os.listdir(path)
        # =============lad=========================
        # files = [f for f in os.listdir(path) if f.endswith(".ts")]
        # files = sorted(files)
        # print(files)
        # with open(f"{save_path}/{name}.ts", "wb") as outfile:
        #     # 逐个读取TS文件并写入到新文件中
        #     for filename in files:
        #         with open(os.path.join(path, filename), "rb") as infile:
        #             outfile.write(infile.read())
        # ======================================
        if 'file_list.txt' in file_names:
            os.remove(path + 'file_list.txt')
        out_file_name = f'{name}.mp4'
        while out_file_name in os.listdir(save_path):
            out_file_name = '新' + out_file_name
        f = open(path + 'file_list.txt', 'w+', encoding="utf-8")
        for one in file_names:
            # f.write(f"{path}/{one}\n")
            f.write("file '" +path+"/"+ one + "'\n")
        f.close()
        print("生成txt文件成功!")
        start = datetime.now()
        print('开始合成，初始时间为:', datetime.now())
        # ffmpeg_bin_dic = 'D:/sofeware/ffmpeg-2023-11-20-git-e56d91f8a8-essentials_build/bin'

        # os.system(
        #     ffmpeg_bin_dic + 'ffmpeg -f concat -safe 0 -i ' + path + 'file_list.txt' + ' -c ' + ' copy ' + save_path + out_file_name)
        # input_string = 'concat:{' + '|'.join(filelist)+'}'
        # print(input_string)
        # command = ['ffmpeg', '-i', path + '/file_list.txt', '-c', 'copy', f"{save_path}/{name}.mp4"]
        pathText=save_path+"/file_list.txt"
        savetxt=f"{save_path}/{name}.mp4"
        cmd_code = f'ffmpeg -f concat -safe 0 -y -i {pathText} -c copy -strict -2 {savetxt}'
        cmd = "ffmpeg -i {} -c copy {}".format(pathText, savetxt)
        print(cmd_code)
        subprocess.run(cmd)
        print('合成后的当前时间为：', datetime.now())
        print('合成视频完成！用时：' + str(datetime.now() - start))
