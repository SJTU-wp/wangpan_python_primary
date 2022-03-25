# author: wp
# 2022年03月10日 22:40
# 提取每行中完整的年月日和时间字段

import re


def extract_time(li):
    for i in li:
        ret_s = re.sub(r'[年月]', r'/', i)
        ret_s = re.sub(r'[日分]', r' ', ret_s)
        ret_s = re.sub(r'时', r':', ret_s)
        com = re.compile(r'\d{4}/[01]?\d/[0-3]?\d\s(?:0\d|1\d|2[0-4]):[0-5]\d')
        ret = com.findall(ret_s)
        if ret:
            print(ret)


if __name__ == '__main__':
    str1 = """hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。
    hello world, 现在是2020年7月20日18时48分。
    hello world, now is 2020/07/05 18:48。
    hello world!
    现在是2020年7月20日18时48分。
    now is 2020/7/20 18:48。"""

    list1 = re.split('\n', str1)

    extract_time(list1)
