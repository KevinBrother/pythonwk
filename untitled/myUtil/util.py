#_*_coding:utf-8_*_

def isRunNian(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print 'true'
        return True

    else:
        print 'false'
        return False
#isRunNian(2008)