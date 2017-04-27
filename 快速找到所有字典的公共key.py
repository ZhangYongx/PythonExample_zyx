"""
快速找到所有字典的公共key
"""

>>> s1.viewkeys()
dict_keys(['a', 'b', 'f'])
>>> s2.viewkeys()
dict_keys(['a', 'b', 'e', 'd', 'g', 'f'])
>>> s3.viewkeys()
dict_keys(['a', 'b', 'e', 'd', 'f'])
>>> s1.viewkeys() & s2.viewkeys() & s3.viewkeys()
set(['a', 'b', 'f'])

#那么利用这两个函数，在配合与运算，可以完美解决这个问题：
>>> map(dict.viewkeys, [s1, s2, s3])
[dict_keys(['a', 'b', 'f']), dict_keys(['a', 'b', 'e', 'd', 'g', 'f']), dict_keys(['a', 'b', 'e', 'd', 'f'])]
>>> reduce(lambda x,y: x&y, map(dict.viewkeys, [s1, s2, s3]))
set(['a', 'b', 'f'])
