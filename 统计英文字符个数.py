'''
法一: 此方法会一次性载入所有的文本文件，内存不足时，会溢出。
'''
from collections import Counter
import re

words = re.findall(r'\w+',open('123.txt').read().lower())
c = Counter(words)
c.most_common(10)    # 数量最多的前10




'''
法二: 此方法比较好
'''

from collections import Counter
import re

c = Counter()
with open('12.txt') as f:
    for line in f:
        word = re.findall(r'\w+',line.lower())
        c += Counter(word)
print c.most_common(10)
