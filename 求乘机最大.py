# -*- coding:utf-8 -*-
'''
设定一个长度为 N 的数字串，将其分为两部分，找出一个切分位置，使两部分的乘积值最大，并返回最大值。
解决问题的核心在于如何将数字串依次分为两部分，大部分同学的思路为将数字串转为字符串，然后使用切片。
也有同学直接使用整数除法 // 和 求余 % 分别得到两部分，以下分别给出代码
'''

#法一:
def product(num):
    # 数字转为字符串
    num2str = str(num)    
    # 预设最大的结果
    max_num = 0
    len_str = len(num2str)    
    for i in range(1,len_str):        
        # 分别得到字符串两边
        left = num2str[:i]
        right = num2str[i:]
        res = int(left) * int(right)        
        # 如果现在的乘积超过目前的乘积，则更新最大值
        if res > max_num:
            max_num = res    
    return max_num

print(product(123456))


#法二:
def product(num):
    # 转为字符串并获取长度
    len_str = len(str(num))    
    # 预设最大值
    max_num = 0
    for i in range(1,len_str):        
        # 分别得到数字两边
        left = num//(10**i)
        right = num%(10**i)
        res = left * right        
        # 判断是否更新
        if res > max_num:
            max_num = res    
    return max_num

print(product(123456))


#附加题:上述题中，对数字串重新打乱排序

def product_2(num):
    num2str = str(num)
    max_num = 0
    for n in itertools.permutations(num2str):
        mixnumber = "".join(n)        
        # 调用之前的 product 函数
        res = product(int(mixnumber))        
        if res > max_num:
            max_num = res    
    return max_num