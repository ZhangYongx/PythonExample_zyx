# 给相同的分组
a = [0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 0, 0]

#法一
g = [a[:1]]
[g[-1].append(y) if x == y else g.append([y]) for x, y in zip(a[:-1], a[1:])]
print(g)


#法二
from itertools import groupby

for k,v in group(a):
    print k,":",list(v)
