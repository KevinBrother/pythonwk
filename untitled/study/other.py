#_*_coding:utf-8_*_
#斐波那切数列
# def FBList(max):
#     n, a, b = 0, 0, 1
#
#     while n < max:
#         print b
#         a, b = b, a + b
#         n = n + 1
#
#
# FBList(6);

# def char2num(s):
#     print {'0': 0, '1': 777, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
#
# map(char2num, '13579')

# def tran(s):
#     S = s.title()
#     return S
#
# nameList = ['adam', 'LISA', 'barT']
#
# print map(tran, nameList)

# def prod(x, y):
#     return x * y
#
# numList = [1, 2, 3]
# print reduce(prod, numList);

# def is_odd(num):
#     return num%2 == 1
#
# nums = [1, 2, 3, 4]
# print filter(is_odd, nums);

# import functools
# def log(func):
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print 'call %s:' % func.__name__
#         return func(*args, **kwargs)
#
#     print 'end %s:' % func.__name__
#     return wrapper
#
#
# @log
# def now(x, y):
#     return x * y
#
# print now(2, 3) , now.__name__


# from PIL import Image
#
# im = Image.open('C:\\Users\\heheda\\Desktop\\ih5\\1.png')
#
# print im.format, im.size, im.mode
#
# im.thumbnail((200, 100))
# im.save('C:\\Users\\heheda\\Desktop\\ih5\\from1.jpg')

# rgb_im = im.convert('RGB')
# rgb_im.thumbnail((200, 100))
# rgb_im.save('C:\\Users\\heheda\\Desktop\\ih5\\from1.jpg', 'JPEG')


# class Student(object):
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('整数啊')
#
#         if value < 0 or value > 100:
#             raise  ValueError('范围啊')
#
#         self.score = value
#
#
# s = Student()
# s.set_score(60)
# print s.get_score()

# class Student():
#
#     @property
#     def score(self):
#         return self.score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('整数啊')
#
#         if value < 0 or value > 100:
#             raise ValueError('范围啊')
#
#         self.score = value
#
# s = Student()
#
# s.score = 9999
# print s.score

# import logging, pdb
#
# logging.basicConfig(level=logging.INFO)
#
#
# s = '0'
#
# n = int(s)
#
# pdb.set_trace()
# logging.info('n = %d' % n)
# print 10/n

import os
print os.name
print os.path.abspath(".")





















