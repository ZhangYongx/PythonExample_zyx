# 读入一个字符串str，输出字符串str中的连续最长的数字串
# 读入一个字符串str，输出字符串str中的连续最长的数字或者字符串
# 读入一个字符串str，输出字符串str中的连续最长,且按升序排列的数字或者字符串

import re

def findMaxSeries(inputStr):
    s = ((len(series), series) for series in re.findall(r'\d+', inputStr))
    max_s = max(s)[1]
    return max_s
    
def findStrSeries(inputStr):
    s = ((len(series),series) for series in re.findall(r'\d+|[A-Za-z]+', inputStr)
    max_s = max(s)[1]
    return max_s
    

def findMaxOrderSeries(inputStr):
    maxLenSeries = ''
    maxLen = 0
    key = ''
    for index, c in enumerate(inputStr):
        if(index == 0):
            key = c
        if(ord(c) == ord(inputStr[index-1])+1):
            key = key + c
        else:
            # 当前字符与之前的字符不构成串
            if(len(key) > maxLen):
                maxLenSeries = key
                maxLen = len(key)
            key = c
    if(key and len(key) > maxLen):
        maxLenSeries = key
    return maxLenSeries
