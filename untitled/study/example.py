#_*_coding:utf-8_*_

# 一
# count = 0
#
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and j != k:
#                 count = count+1
#                 print (count, int(str(i)+str(j)+str(k)))

# 二
# mount = int(raw_input('请输入金额：'))
#
# arr = [0, 100000, 200000, 400000, 600000, 1000000]
# arr.reverse()
#
# rat = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
# rat.reverse()
#
# count = 0
#
# for i in range(0, 6):
#     if mount > arr[i]:
#         count += (mount - arr[i]) * rat[i]
#         mount = arr[i]
#
# print  '值为：' + str(count)

# 三

# 四
#输入某年某月某日，判断这一天是这一年的第几天？

# 判断哪年 是否为闰年
# 前几个月有多少天
# 加上天数
# from untitled.myUtil import util
#
# year = int(raw_input('请输入年\n'))
# mount = int(raw_input('请输入月\n'))
# day = int(raw_input('请输入日\n'))
#
# arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# if util.isRunNian(year):
#     print 121232
#     arr[2] += 1
#
# days = 0
#
# for i in range(0, mount):
#     days += arr[i]
#
# print arr
#
# days += day
#
# print days


# 五
#
# l = []
#
# for i in range(0, 3):
#    num = raw_input('请输入数字\n')
#    l.append(num)
#
# l.sort()
# l.reverse()
#
# print l

#六

#第n位数字
# def fib(n):
#     a,b = 1,1
#     if n = 1 or n = 2:
#         return 1
#
#     for i in range(2, n):
#        num =



7








