# author: wp
# 2022年03月08日 23:13
# 通过asyncio实现上课用gevent实现的并行下载器

import asyncio
import urllib.request


async def my_download(url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


async def main():
    task1 = asyncio.create_task(my_download('http://www.baidu.com/'))
    task2 = asyncio.create_task(my_download('http://www.cskaoyan.com/'))
    task3 = asyncio.create_task(my_download('http://www.qq.com/'))

    # await task1
    # await task2
    # await task3

    result = await asyncio.gather(task1, task2, task3)

    print(result)


if __name__ == '__main__':
    asyncio.run(main())
