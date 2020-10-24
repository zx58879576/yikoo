"""
①通过编码形式，大小写差32
"""
str="www.baidu.com"
for item in str :
   if 97<=ord(item)<=122 :
     upper=ord(item)-32
     print(chr(upper),end="")
   else:
     print(item,end="")  
"""
②直接通过字符串函数 upper()转大写
"""     
     print(str.upper())   
#输出 ： WWW.BAIDU.COM


