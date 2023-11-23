
import logging
import os
import re
import subprocess

if __name__ == '__main__':
    # logging.basicConfig(level=logging.ERROR)
    # logger = logging.getLogger("aaa")
    # logger.error("111")
    # os.startfile('cmd',"copy /b  E:/ffmpeg/video/新建文件夹/merge/*  E:/ffmpeg/video/新建文件夹/1.ts")
    # os.system('start cmd.exe /k  copy /b  E:/ffmpeg/video/新建文件夹/merge/*  E:/ffmpeg/video/新建文件夹/1.ts')
    # subprocess.call(f'start cmd.exe /k {cmd}',shell=True)
    # cmdd="copy /b E:\\ffmpeg\\video\\新建文件夹\\merge\\*  E:\\ffmpeg\\video\\新建文件夹\\2.ts"
    # os.system(f"start cmd.exe /k   {cmdd}")
    # sr="E:/ffmpeg/video/新建文件夹/1.ts"
    # replace = sr.replace("/", "\\")
    # print(replace)
    # listdir = os.listdir("E:/ffmpeg/video/新建文件夹/merge")
    # fileStr = "concat:"
    # len__ = listdir.__len__()
    # for index in range(len__):
    #     print(f"index=={index}")
    #     if index==len__-1:
    #         fileStr+=f"{listdir[index]}"
    #     else:
    #         fileStr+=f"{listdir[index]}|"
    #
    # print(f"fileStr=={fileStr}")
    # sta="asdada asda sdasda ads 1513113321"
    # sta="[]['/.//.12.3/.//“？？{}}》《》？，"
    sta="FC2PPV-3299161めっちゃ可愛いアイドルFACEに天使のようなヒロイン美女と天然光の下で・・・"
    sub = re.sub(r'\s+|[，。、|/・？]|[1-9]|[A-Z]*',"", sta)

    print(sub)
    # f=open("D:/printlog/aa.txt",'a')
    # print("asdadsa",file=f)
    # f.close()
    # f = open("D:/printlog/aa.txt", 'a')
    # print("asdadsa",file=f)
    # f.close()
    # f = open("D:/printlog/aa.txt", 'a')
    # print("asdadsa",file=f)
    # f.close()
    # f = open("D:/printlog/aa.txt", 'a')
    # print("asdadsa",file=f)
    # f.close()
    # f = open("D:/printlog/aa.txt", 'a')
    # print("asdadsa",file=f)
    # f.close()
    # f = open("D:/printlog/aa.txt", 'a')
    # print("asdadsa",file=f)
    # f.close()
    # f = open("D:/printlog/aa.txt", 'a')
    # print("asdadsa",file=f)
    # f.close()
    pass