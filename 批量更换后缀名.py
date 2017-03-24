# -*- coding: utf-8 -*-
import os,os.path

abs_path=os.path.abspath('.')  #获取当前绝对路径

for file in os.listdir('.'):
    if os.path.isfile(file):
        posion = os.path.splitext(file)
        if posion[1] == 'mp4':    #如果文件的后缀名为mp4
            newname = posion[0] + '.py' #把后缀名改为py
            os.rename(file,newname)