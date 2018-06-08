#_*_coding:utf-8_*_

import urllib
import urllib2

pastdata = urllib.urlencode({
    'type': 2,
    'id': 30987293,
    'auto': 1,
    'height': 66
})

req = urllib2.Request(
    url = 'http://music.163.com/outchain/player',
    data = pastdata
)

result = urllib2.urlopen(req)

print result.read()