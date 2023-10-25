#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 22:13
# @Author  : backpacker
# @File    : ColorSelect.py
# @Description : $
from tkinter import Tk,messagebox,filedialog
from tkinter.colorchooser import *
from tkinter import *

from PIL import ImageGrab

from Base.MainQuit import MainQuit


class ColorSelect(MainQuit) :

    def hex2rgb(self,hex_color):
        h = hex_color
        rgb = (int((h[1:3]), 16), int((h[3:5]), 16), int((h[5:7]), 16))
        return rgb

    def rgb2hex(self,rgb):
        hex_color = "#" + hex(rgb[0])[2:].zfill(2) + hex(rgb[1])[2:].zfill(2) + hex(rgb[2])[2:].zfill(2)
        return hex_color.upper()

    def callback(self,event,root,colorHex, colorRGB, colorTv,w,h):
        root.destroy()
        img = ImageGrab.grab()
        img = img.resize((w, h))# 对截图大小重置为窗口大小。
        px = img.load()
        img.close()
        rgbroot = px[event.x, event.y]
    
        rgb_hex = self.rgb2hex(rgbroot)
    
        rgb_1 = self.hex2rgb(rgb_hex)
    
        self.setTvContent(colorHex,rgb_hex)
        self.setTvContent(colorRGB,rgb_1)
        colorTv.config(background=f"{rgb_hex}")
    
    
    def gatherColor(self,colorHex:Text,colorRGB:Text,colorTv:Label):
        root =Toplevel()
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root.geometry(f"{w}x{h}+0+0")
        root.overrideredirect(True) # 隐藏窗口栏
        root.attributes('-alpha',0.01)# 设置透明度 最小0.01 设置为0 界面会消失掉
        root.configure(cursor="crosshair") # 设置鼠标样式
        root.bind("<Button-1>",lambda event:self.callback(event,root,colorHex,colorRGB,colorTv,w,h))
        root.bind("<Button-3>",lambda event:self.callback(event,root,colorHex,colorRGB,colorTv,w,h))
        mainloop()
    
    
    def selectColor(self,colorHex:Text,colorRGB:Text,colorLB:Label):
        selectColor = askcolor()
    
        self.setTvContent(colorHex,selectColor.__getitem__(1))
    
        self.setTvContent(colorRGB,selectColor.__getitem__(0))
    
        colorLB.config(background=f"{selectColor.__getitem__(1)}")
    
        pass
    
    def setTvContent(self,tv:Text,char:str):
        tv.delete(0.0,END)
        tv.insert(END,char)
    
    
    
    def showDialog(self,mainRoot):
        root=Tk()
        root.geometry("640x540")
        root.title("颜色采集")
    
        withd=20
        height=1
    
        Label(root,text="颜色值HEX: ",width=withd,height=height,font=10,background="light gray").grid(row=0,column=0,pady=8)
        Label(root,text="颜色值RGB: ",width=withd,height=height,font=10,background="light gray").grid(row=1,column=0,pady=8)
        Label(root,text="颜色     : ",width=withd,height=height,font=10,background="light gray").grid(row=2,column=0,pady=8)
        Label(root,text="选择颜色值: ",width=withd,height=height,font=10,background="light gray").grid(row=3,column=0,pady=8)
        Label(root,text="选择颜色值: ",width=withd,height=height,font=10,background="light gray").grid(row=4,column=0,pady=8)
    
        colorHex = Text(root, width=withd,height=height,font=10, background="light gray")
        colorHex.grid(row=0,column=1,pady=8,padx=4)
    
        colorRGB = Text(root,width=withd,height=height, font=10, background="light gray")
        colorRGB.grid(row=1,column=1,pady=8,padx=4)
    
        colorTv = Label(root, width=withd,height=height,font=10, background="light gray")
        colorTv.grid(row=2,column=1,pady=8,padx=4)
    
        Button(root,text="点击采集", width=withd,height=height,font=10, background="light gray",
                          command=lambda :self.gatherColor(colorHex,colorRGB,colorTv)).grid(row=3,column=1,pady=8,padx=4)
        Button(root,text="点击选择", width=withd,height=height,font=10, background="light gray",
                          command=lambda :self.selectColor(colorHex,colorRGB,colorTv)).grid(row=4,column=1,pady=8,padx=4)

        # 使用协议机制与窗口交互，并回调用户自定义的函数
        super().registLisetener(root,mainRoot)
        mainloop()
# if __name__ == '__main__':
#     showDialog()
