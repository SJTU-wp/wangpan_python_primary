# author: wp
# 2022年03月04日 21:17

import socket
import select
import sys


def tcp_client():
    if len(sys.argv) == 1:
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = (sys.argv[1], 2000)  # IP地址是传的参数, linux下运行时python传参
    client.connect(dest_addr)

    # 创建一个epoll对象
    epoll = select.epoll()

    # 让epoll监控client sys.stdin
    epoll.register(client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)

    while True:  # 写这句的功效还没有太理解
        # events是列表里边存元组 (fd, event)
        events = epoll.poll(-1)  # -1表示永久等待, max events可以不写
        for fd, event in events:
            if fd == client.fileno():  # 小弟监控到了client缓冲区中有连接信息
                data = client.recv(100)
                if data:  # 如果数据不为空/如果接收到了数据
                    print(data.decode('utf8'))
                else:
                    print('对方断开了')  # 如果数据为空，没有接收到数据，说明对方已断开
                    return  # 返回上一级函数
            elif fd == sys.stdin.fileno():  # 小弟监控到了标准输入缓冲区中有连接信息
                data = input()  # 服务器端说话，发给客户端
                client.send(data.encode('utf8'))

    client.close()


if __name__ == '__main__':
    tcp_client()
