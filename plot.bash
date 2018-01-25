#! /usr/bin/gnuplot
# ------------------------------------------------------------------------------
# Jake McKennon
# 28 November 2017
# ------------------------------------------------------------------------------

set xlabel "Time"
set ylabel "RPS (1-minute rate)"
set title "RPS vs. Time"
set xdata time
set timefmt "%s"
set term png
set output 'plot.png'

plot "newstats.txt" u 1:2 w l t '500s', "newstats.txt" u 1:3 w l t '200s', "newstats.txt" u 1:4 w l t '400s'
