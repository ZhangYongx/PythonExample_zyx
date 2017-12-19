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

# windows中，目录路径是 双斜杠.  type(base_path) 为 str 类型
base_path = "E:\\06.python3.5全栈工程师零基础到项目实战全套\\02.好评赠品\\02.python精品电子书"
# 由于 base_path目录 包含中文 ，需要转换为 gbk
path = base_path.decode('utf-8').encode('gbk')

lst = os.listdir(path)
for i in lst:
    """
    os 默认的编码方式是 str, 最后避免 print打印出乱码，需要转换为 utf-8
    """
    print i.decode('gbk').encode('utf-8')

 
if __name__ == '__main__':
    search()

 
