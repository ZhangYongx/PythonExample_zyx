"""
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
"""

# 法一：元素因式分解后，统计所有 2，5 的个数
num=[0,0]
for i in range(L.__len__()):
    while(L[i]%2==0):
        num[0]=num[0]+1
        L[i]=L[i]//2
    while (L[i] % 5 == 0):
        num[1] = num[1] + 1
        L[i] = L[i] // 5
print(min(num))

# 法二：两两相乘，通过除以10，求出个数。
x=reduce(lambda a,b:a*b,L)
yu=0
count=0
while yu==0:
    if x%10==0:
        count+=1
    else:
        yu=1
    x/=10
print count

# 法三：两两相乘，通过字符串，求出末尾零的个数。
l = 1
for i in L:
    l *= i
new_l = str(l).rstrip('0')
print(len(str(l)) - len(new_l))
