#! /usr/bin/python
# ------------------------------------------------------------------------------
# Jake McKennon
# 28 November 2017
# ------------------------------------------------------------------------------

import urllib2
import sys
import time
import os
import subprocess
from itertools import izip

newf = open('newstats.txt', 'w').close()
newf = open('newstats.txt', 'a')

L = open('stats.txt').readlines()

# Only works entirely properly based on 10 second intervals; need to change
# the indexing of the second variable for other intervals.
for line, offset in izip(L, L[6:]):
    splitL = line.split('\t')
    splitO = offset.split('\t')

    if offset[0] < line[0]:
        break
    if line == '' or offset == '':
        continue

    five = (int(splitO[1]) - int(splitL[1])) / 60
    two = (int(splitO[2]) - int(splitL[2])) / 60
    four = (int(splitO[3]) - int(splitL[3])) / 60

    newline = splitL[0] + '\t' + str(five) + '\t' + str(two) + '\t' + str(four) + '\n'
    newf.write(newline)


subprocess.Popen("./plot.bash; rm newstats.txt", shell=True)
