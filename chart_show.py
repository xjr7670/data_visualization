#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from matplotlib.pyplot import *

x = [1, 2, 3, 4]
y = [5, 4, 3, 2]

figure()

# divide subplots into 2 x 3 grid
# and select #1
subplot(231)
plot(x, y)

# select #2
subplot(232)
bar(x, y)

# horizontal bar-charts
subplot(233)
barh(x, y)

# create stacked bar charts
subplot(234)
bar(x, y)

# we need more dta for stacked bar charts
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')

# box plot
subplot(235)
boxplot(x)

# scatter plot
subplot(236)
scatter(x, y)

show()
