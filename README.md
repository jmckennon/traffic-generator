# traffic-generator

This program is designed to generate traffic to run against a web server using the urllib library for Python. The files stats.txt and plot.png contain a sample of generated data from over the course of an hour using an average request rate of ~700 across 200s, 400s, and 500s.

## To run your own simulation:
1. Run timeserver.py on a Linux box.
2. On 3 other boxes, run trafficgen.py, supplying one with a 200 url, one with a 400 url, and one with a 500 url. Additionally, give it the pseudo-RPS and jitter (between 0 and 1).
3. Run stats.py on another box, giving it the interval of collection as an argument.
4. Let the programs run; data is collected in stats.txt.
5. Once data is done being collected, run plot.py, which also calls plot.bash to generate the gnuplot graph of RPS vs. Time and saves it as plot.png.
