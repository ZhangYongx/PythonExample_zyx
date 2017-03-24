# -*- code:utf-8 -*-
#法一：
def pr(n):
    f = 2
    while f*f <= n:
        while not n % f:
            yield f
            n //= f
        f += 1
    if n >1:
        yield n

print list(pr(20))


#法二：
import math  
number = int(raw_input("Enter a number: "))  
list = []  
  
def getChildren(num):  
    print '*'*30  
    isZhishu = True  
    i = 2  
    square = int(math.sqrt(num)) + 1  
    while i <= square:  
        if num % i == 0:  
            list.append(i)  
            isZhishu = False  
            getChildren(num / i)  
            i += 1  
            break  			#通过此 break 跳出 if 语句，然后继续 for 的迭代
        i += 1  
    if isZhishu:  
        list.append(num)  
  
getChildren(number)  
print list


#法三：

def fj(num):
    while num != 1:
        for i in range(2,num+1):
            if (num%i) == 0:
                num = num / i
                # if num == 1:
                #     print i
                # else:
                print i,
                break       #通过此 break 跳出 if 语句，然后继续 for 的迭代