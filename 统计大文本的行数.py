#!_*_coding:utf-8_*_
f=open('t.txt','rb')

def linecount():
    #最后一行没有换行符，所以 counts 从 1 开始
    counts = 1
    while True:
        buffer = f.read(65535)
        if not buffer:
            break
        counts += buffer.count('\n')
    return counts

print linecount()
