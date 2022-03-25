# author: wp
# 2022年03月04日 22:42
# 使用epoll实现聊天室

import socket
import select
import sys


def chatroom_tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)

    # 创建一个epoll对象
    epoll = select.epoll()

    # 让epoll监控s sys.stdin
    epoll.register(s.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)

    client_list = []  # 存储所有的client对象

    while True:  # 写这句的功效还没有太理解
        # events是列表里边存元组 (fd, event)
        events = epoll.poll(-1)  # -1表示永久等待, max events可以不写
        for fd, event in events:
            if fd == s.fileno():  # 有客户端连接
                new_client, client_addr = s.accept()
                print(client_addr)
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            else:
                remove_client = None
                for client in client_list:
                    if fd == client.fileno():
                        data = client.recv(1000)  # 接收对应客户端发过来的数据
                        print(data.decode('utf8'))
                        if data:  # 拿到数据，群发给其他的客户端（处于连接状态的）
                            for other_client in client_list:
                                if other_client is client:
                                    pass
                                else:
                                    other_client.send(data)
                        else:  # 该对应客户端断开了
                            remove_client = client
                if remove_client:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()

    s.close()


if __name__ == '__main__':
    chatroom_tcp_server()
