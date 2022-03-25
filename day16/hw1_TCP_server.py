# author: wp
# 2022年03月03日 20:43
# TCP服务器端代码编写

import socket


def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM表示这是TCP的socket
    addr = ('192.168.5.9', 2000)
    s.bind(addr)  # 绑定，端口此时并未激活
    s.listen(128)  # listen时，端口才激活

    new_client, client_addr = s.accept()  # 与客户端的connect共同实现三次挥手
    print(client_addr)

    # 接下来类似之前的UDP，就可以进行send, recv操作
    new_client.send('hello, world!'.encode('utf8'))  # 这里为何是new_client发送而不是s发送呢？
    # new_client承担之后的任务，它是从缓冲区中读出来的一个客户端的连接信息，不再是s了
    data = new_client.recv(100)
    print(data.decode('utf8'))  # 编码与解码

    new_client.close()
    s.close()


if __name__ == '__main__':
    tcp_server()
