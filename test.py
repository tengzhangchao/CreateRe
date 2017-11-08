#! -*- coding:utf-8 -*-

from CreateRe import create_re


STRING = u'''
abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42
335.225.1537	+1-(800)-555-2468
111.230.4168    +2-(230)-111-2463
tzc@maskghost.com
http://thief.one nmask
192839383
http://tool.nmask.cn nm4k
nmask,nm4k
http://home.nmask.cn nmask
'''

S = ["http://tool.nmask.cn","http://thief.one"]

'''如果想要匹配的结果为多个，则tag设置为True，缺省为False'''
tag=True

cur=create_re()
RES=cur.run(STRING,S,tag=tag)
check_result=cur.check_res(RES,tag=tag)

print(RES)
print(check_result)


# ''' 获取已有的正则表达式 '''

# print(cur.get_res("email"))

