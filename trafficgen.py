#! /usr/bin/python
# ------------------------------------------------------------------------------
# Jake McKennon
# 28 November 2017
# ------------------------------------------------------------------------------

import sys
import time
import random

url = sys.argv[1]
rps = sys.argv[2]
jitter = sys.argv[3]

lower = (float(rps) * (1.0 - float(jitter)))
upper = (float(rps) * (1.0 + float(jitter)))

while True:
    realrps = random.uniform(lower, upper)
    t = time.time()

    for i in range(1, int(realrps)):
        try:
            site = urllib2.urlopen(url)
        except urllib2.URLError:
            pass

    while(time.time() < t + 1):
        pass
