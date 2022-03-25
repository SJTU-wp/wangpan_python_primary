# author: wp
# 2022年03月11日 23:32
# 0-99的数字匹配
import re
num_list = [-6, 0, 8, 37, 99, 189, '06']
for num in num_list:
    num = str(num)
    ret = re.match(r'[1-9]?\d$', num)
    if ret:
        print(ret.group(), end=' ')
