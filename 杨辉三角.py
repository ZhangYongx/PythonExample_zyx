# -*- coding:utf-8 -*-

‘’‘
法一：
生成一个全为0的list，长度为函数的双倍+1，保证数字往中间靠拢。最后把多余的0替换为空格；
一行一行的处理，后面一行会用到上面一行的数据；
有两个迭代来处理。一个来确定行数，一个来确定该行数下，数字固定在哪个地方；
‘’‘


def yh(row):
    result_list = [0] * (row * 2 + 1)
    
    for row_base in range(row):
        #base_local为数字「固定打印」的位置。
        base_local = row - row_base
        #第一行，数字1 定在列表的中间
        if row_base == 0:
            result_list[base_local] = 1
        else:
        	#杨辉三角每行数字的个数 = （行数+1 ）*2 -1
            now_local = (row_base + 1)*2 - 1
            #通过数字个数，可以确定数字的位置范围。打印的时候，隔一个数打印。最后替换掉所有的0。
            for i in range(0,now_local,2):
                #以base_local作为原点，now就是相对base_local的「固定位置」。
                now = base_local + i
                result_list[now] = result_list[now - 1] + result_list[now + 1]
                #本行中，数字的前一个为上行的数字，但本行不需要，所以重置为0，避免影响结果。
                result_list[now - 1] = 0

#打印最后的list。注意把 0, 替换掉，而不是0。否则会替换掉数字里面的0
        print str(result_list) \
            .replace('[',' ').replace(' 0,','  ').replace(',',' ').replace('0]','  ')

yh(15)



‘’‘
法二：
‘’‘
def printLine(lineList,row):
    #把 list元素类型 全部转换为 str
    lineList = [str(tmpNum) for tmpNum in lineList]
    #空格自动填充在该行数字的前面，填充数量为行长度减去list长度。然后合并list。list数字用空格分开。
    print("%s%s" % (" " * (row - len(lineList)), " ".join(lineList)))

def pascal(row):
    for i in range(row):
        if i < 2:
            yhList = [1] * (i + 1)
        else:
        	#这个解析式很巧妙:
        	#nlist = yhlist[1:]
        	#yhlist[j+1] = yhlist[j] + nlist[j]
        	#并且 yhlist[1:-1] 自动生成列表。用列表解析式最好不过！
            yhList[1:-1] = [(tem + yhList[j]) for j,tem in enumerate(yhList[1:])]
        printLine(yhList,row)

pascal(15)
