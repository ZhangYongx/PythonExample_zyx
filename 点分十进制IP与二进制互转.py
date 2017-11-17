# coding:utf-8
from IPy import IP
import re

ip = "Please input your ipaddress: "
# 点分十进制 ==> 二进制
bin_ip = IP(ip).strBin()

#二进制 ==> 点分十进制
# re.findall(r'.{8}', ip)  固定长度切割 ip地址
# int(i,2) 二进制转10尽职

".".join([str(int(i,2) for i in re.findall(r'.{8}', ip)])
