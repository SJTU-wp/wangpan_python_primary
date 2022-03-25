# author: wp
# 2022年03月11日 23:20
# 写一个正则表达式，使其能同时识别下面所有的字符串：'bat','bit', 'but', 'hat', 'hit', 'hut'

import re

str1 = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
for i in str1:
    ret = re.match('[bh][aiu]t', i)
    if ret:
        print(ret.group(), end=' ')
