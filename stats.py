#! /usr/bin/python
# ------------------------------------------------------------------------------
# Jake McKennon
# 28 November 2017
# ------------------------------------------------------------------------------

import urllib2
import sys
import time
import random

interval = sys.argv[1]

open('stats.txt', 'w').close()  # clears the file
f = open('stats.txt', 'a')

while True:
    t = time.time()
    stats = urllib2.urlopen('http://uw1-320-04:42651/stats')
    htmlstats = stats.read()
    newline = ''
    for line in htmlstats.split('\n'):
        if line == '':
            continue
        num = line.split(': ')
        print num
        newline += num[1]
        newline += '\t'

    newline += '\n'
    f.write(newline)

    while(time.time() < t + float(interval)):
        pass
