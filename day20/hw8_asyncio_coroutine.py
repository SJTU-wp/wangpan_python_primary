# author: wp
# 2022年03月08日 21:58
# 使用asyncio启动两个协程（和上课一样），理解协程原理即可

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print("started at {}".format(time.strftime('%X')))

    await task1
    await task2  # 等待两个协程均完成，耗时约2s——因为是并发的

    print("finished at {}".format(time.strftime('%X')))


if __name__ == '__main__':
    asyncio.run(main())
