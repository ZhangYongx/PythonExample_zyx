#生成200个随机的10位数优惠卷

import random, string

#法一
for i in range(200):
    chars = string.letters + string.digits
    s = [random.choice(chars) for i in range(10)]
    ''.join(s)

#法二
def suiji(len=8,chars=string.letters+string.digits):
	"".join([random.choice(chars) for i in range(len)]
