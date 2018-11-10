#!/usr/bin/python3

import tushare as ts
import csv
import openpyxl

# 实时票房
df = ts.realtime_boxoffice()
print("实时电影票房\n")
print(df)

# 沪深上市公司基本情况
df1 = ts.get_stock_basics()
print("\n")
print("沪深上市公司基本情况\n")
print(df1.head())
df1.to_excel("沪深上市公司基本情况.xlsx")
