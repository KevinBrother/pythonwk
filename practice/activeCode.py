#_*_coding:utf-8_*_

# XXXX-XXXX-XXXX-XXXX  16位、英文大写

#  做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
# 1. 定义 生成 激活码的函数，2. 循环调用

# def newCode:

import string, random
initspecial = string.punctuation
special = []

for i in initspecial:
    special.append(i)

STR = [chr(i) for i in range(65, 91)] #65-91对应字符A-Z

str = [chr(i) for i in range(97, 123)] #a-z

number = [chr(i) for i in range(48, 58)] #0-9

total = STR + str + number + special

# print len(total)

strCode = ''

for i in range(1, 21):
    if(i % 4 == 0):
        strCode = strCode + "-"
    else:
        strCode = strCode + total[random.randint(0, len(total)-1)]

print 'strCode is %s and length is %d' %(strCode, len(strCode))


# 保存到 MySQL 关系型数据库中

