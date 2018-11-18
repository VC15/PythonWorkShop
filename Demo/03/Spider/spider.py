#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
r = requests.get('https://book.douban.com/subject/6709783/comments/').text
#print(r)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r, 'lxml')
pattern = soup.find_all('span', 'short')
for item in pattern:
    print(item.string)
