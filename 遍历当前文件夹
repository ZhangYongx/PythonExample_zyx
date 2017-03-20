# -*- coding: utf-8 -*-
"""
遍历当前目录及子目录
搜索名称含有关键词的文件
打印完整路径
用法：$ python search.py [关键词]
"""
import os, sys
keyword = sys.argv[1]

def search(pathname = '.'):
    for fi in os.listdir(pathname):
        fi_d = os.path.join(pathname,fi)
        if os.path.isdir(fi_d):
            search(fi_d)
        elif keyword in os.path.basename(fi_d):
                print os.path.abspath(fi_d)

if __name__ == '__main__':
    search()
