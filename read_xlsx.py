#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import xlrd

file = './example_code/chapter2/ch02-xlsxdata.xlsx'

wb = xlrd.open_workbook(filename=file)
ws = wb.sheet_by_name('Sheet1')

dataset = []

for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r, c).value)
    dataset.append(col)

from pprint import pprint
pprint(dataset)
