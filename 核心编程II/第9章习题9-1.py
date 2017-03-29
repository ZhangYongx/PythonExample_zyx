# coding=utf-8

def openf(f):
    f1 = open(f,'r')
    for i in f1:
        i = i.strip():   #删除空行
        if i[0] != '#':   #去掉行头的空格符
            print i,     #去掉print自带的回车符
    f1.close()


ff = 'C:\Users\Administrator\PycharmProjects\puppet.conf'
openf(ff)