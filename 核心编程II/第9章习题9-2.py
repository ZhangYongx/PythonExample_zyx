# coding=utf-8

def openf(file,num):
    f = open(file,'r+')
    n = 0
    for i in f:
        if n == num:
            break
        print i,
        n += 1
    f.close()

file = 'C:\\Users\\Administrator\\PycharmProjects\\puppet.conf'
openf(file,500)