#_*_coding:utf-8_*_

import urllib2

my_url = 'http://www.google.com'
response = urllib2.urlopen(my_url)
redirected = response.geturl() == my_url
print redirected

