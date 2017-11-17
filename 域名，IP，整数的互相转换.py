#从URL提取域名或ip
#把 域名 <==> ip 互相转换
#把 整数 <==> ip 互相转换

#从URL提取域名或ip
from urlparse import *
url = 'http://segmentfault.com/blog/biu/1190000000330941'
r = urlparse(url)
print r
'''
ParseResult(scheme='http', netloc='segmentfault.com', path='/blog/biu/1190000000330941', params='', query='', fragment='')
'''

#把 域名 ==> ip 互相转换
def getIp(domain):
    import socket
    myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    print(myaddr)
    
#把 ip ==> 域名 互相转换    
import sys, socket
try:
    result = socket.gethostbyaddr('66.249.71.15')
    print 'Primary hostname:'
    print '  ' + result[0]

    # Display the list of available addresses that is also returned
    print '\nAddresses:'
    for item in result[2]:
        print '  ' + item
except socket.herror, e:
    print 'Couldn't look up name:', e
    
    
#把 整数 <==> ip 互相转换
import socket,struct
int_ip = 123456789
ip = '192.168.1.1'
#整数 转 ip
num_to_ip = socket.inet_ntoa(struct.pack('I',socket.htonl(int_ip)))
#ip转整数
ip_to_num = socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0])



import struct
import socket
# 字符串ip 转 长整形int
def ip_to_int(ip):
    return struct.unpack('!I', socket.inet_aton(ip))[0]
	
# 长整形int 转 字符串ip	
def int_to_ip(ip_int):
    return socket.inet_ntoa(struct.pack('!L', ip_int))
