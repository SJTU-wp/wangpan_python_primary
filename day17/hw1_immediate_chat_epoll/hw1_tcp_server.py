# author: wp
# 2022年03月04日 21:17
# 使用epoll编写即时聊天，实现两边想说就说

import socket
import select
import sys


def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', 2000)  # 这里为什么要变成空的？ 之后会在客户端那边传参
    s.bind(addr)
    s.listen(128)
    new_client, client_addr = s.accept()
    print(client_addr)

    # 创建一个epoll对象
    epoll = select.epoll()

    # 让epoll监控new_client sys.stdin
    epoll.register(new_client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)

    while True:  # 写这句的功效还没有太理解
        # events是列表里边存元组 (fd, event)
        events = epoll.poll(-1)  # -1表示永久等待, max events可以不写
        for fd, event in events:
            if fd == new_client.fileno():  # 小弟监控到了new_client缓冲区中有连接信息
                data = new_client.recv(100)
                if data:  # 如果数据不为空/如果接收到了数据
                    print(data.decode('utf8'))
                else:
                    print('对方断开了')  # 如果数据为空，没有接收到数据，说明对方已断开
                    return  # 返回上一级函数
            elif fd == sys.stdin.fileno():  # 小弟监控到了标准输入缓冲区中有连接信息
                try:
                    data = input()  # 服务器端说话，发给客户端
                except EOFError:  # 按CTRL+D后服务器断开
                    print('我断开了')
                    return
                new_client.send(data.encode('utf8'))

    new_client.close()
    s.close()


if __name__ == '__main__':
    tcp_server()
