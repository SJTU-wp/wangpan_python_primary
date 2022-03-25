# author: wp
# 2022年03月10日 23:42
# 提取出字符串中的单词

import re

str1 = 'hello world ha ha'
ret = re.split(' ', str1)
print(ret)
