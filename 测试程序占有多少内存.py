"""
测试程序占有多少内存
"""

import resource
mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
l = []
for i in range(500000):
    l.append(object())
mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
del l
print('Class: {}:\n'.format(getattr(cls, '__name__')))
print('Initial RAM usage: {:14,}'.format(mem_init))
print('  Final RAM usage: {:14,}'.format(mem_final))

"""
不同平台上ru_maxrss的值的单位是不一样的，在OS X上单位是Byte，但是在Linux上单位是KB。我之前用惯了OS X，一次查看现在程序内存使用，看到上述方法的返回值太小，数量级上差了好多，觉得明显不对啊，困惑了很久，最后还是直接去翻libbc的手册(https://www.gnu.org/software/libc/manual/html_node/Resource-Usage.html)才知道这个区别。大家要注意。
上面用到的resource.RUSAGE_SELF表示当前进程自己，如果你希望知道该进程下已结束子进程的内存也计算进来，需要使用resource.RUSAGE_CHILDREN。另外还有一个RUSAGE_BOTH相当于当前进程和子进程自己的总和，不过这个是平台相关的，你要先了解你是用的发行版本是否提供。
"""