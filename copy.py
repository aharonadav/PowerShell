#!/usr/bin/python

import os,time,StringIO

list= []

out=os.popen('cd <folder path).read()

timestr= time.strftime("%Y%m%d")

f= os.path.abspath("<destination folder path/%s/"%timestr)

os.system('cd ?Destination folder path && mkdir %s'% timestr)

for line in StringIO.StringIO(out):
        list.append(line)

listlen= len(list)
index= 0

for x in list:
    x = list[index]
    x= x.strip('\n')
    print x
    os.system('cp "%s" "%s"' % (str(x),str(f)))
    index = index+1
