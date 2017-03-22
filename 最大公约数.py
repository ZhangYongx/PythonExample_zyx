"""
使用短除法求最大公约数
"""

if a < b:
	a , b = b , a
	
while b:
	a,b = b,a%b
print a
