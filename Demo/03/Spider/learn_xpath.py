#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
from lxml import etree

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url).text
#print(r)

s = etree.HTML(r)
#print(s.xpath('//*[@id="comments"]/ul/li[1]/div[2]/p/span/text()'))
#print(s.xpath('//*[@id="comments"]/ul/li[3]/div[2]/p/span/text()'))
#print(s.xpath('//div[@class="comment"]/p/span/text()')[0])
#print(s.xpath('//*[@id="comments"]/ul/li/div[2]/p/span/text()'))
#print(s.xpath('//div[@class="comment"]/p/span/text()'))


file = s.xpath('//div[@class="comment"]/p/span/text()')


"""
with open('pinglun.txt', 'w', encoding='utf-8') as f:
    for i in file:
        print(i, '\n')
        f.write(i + '\n')
"""

import pandas as pd
df = pd.DataFrame(file)
df.to_excel('小王子评论.xlsx', sheet_name = 'Sheet1')
