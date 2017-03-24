# -*- coding: utf-8 -*-
#使用递归找出字符的所有子集
def p(s):
    print s[0] ,
    c = 1
    if len(s) == c:return
    while len(s) > c:
        for i in s[c:]:
            out_s = s[:c] + i
            print out_s ,
        c +=1
    p(s[1:])

s = raw_input(">")
p(s)



#法二
# -*- coding: utf-8 -*-
def p(s_arr):
    if len(s_arr) == 1:
        return 1
    for i, item_i in enumerate(s_arr):
        print "".join(s_arr[:i+1]),
    p(s_arr[1:])

if __name__ == "__main__":
    strs = raw_input("input> ")
    p((list(strs)))
