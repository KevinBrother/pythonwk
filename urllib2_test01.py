#!/usr/bin/python
# -*- coding:utf8 -*-
import urllib2
import urllib

url = 'http://www.runoob.com/try/runcode.php'

values = {'name': 'WHY',
          'location': 'SDU',
          'language': 'Python'}

data = urllib.urlencode(values)

print data
# 发送请求同事传达data表单
req = urllib2.Request(url, data)
# 接收反馈的信息
response = urllib2.urlopen(req)
# 读取反馈的内容
the_page = response.read()

print the_page





# data = {}
#
# data['name'] = 'WHY'
# data['location'] = 'SDU'
# data['language'] = 'Python'
#
# url_values = urllib.urlencode(data)
# print url_values
