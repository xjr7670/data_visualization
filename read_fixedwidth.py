#!/usr/bin/env python2
#-*- coding:utf-8 -*-

import struct
import string

datafile = './example_code/chapter2/ch02-fixed-width-1M.data'

# this is where we define how to 
# understand line of data from the file
mask = '9s14s5s'

with open(datafile, 'r') as f:
    for line in f:
        fields = struct.Struct(mask).unpack_from(line)
        print 'fileds: ', [field.strip() for field in fields]
