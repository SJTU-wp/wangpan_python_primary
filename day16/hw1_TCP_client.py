# author: wp
# 2022年03月03日 20:44
# TCP客户端代码编写

import socket


def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_addr = ('192.168.5.9', 2000)
    client.connect(dest_addr)  # 与s.accept()共同实现三次挥手
    # 连接已建立
    data = client.recv(5)  # 客户端接收服务器端的消息，先接5个字节
    print(data.decode('utf8'))

    data = client.recv(5)
    print(data.decode('utf8'))

    client.send('我是男生abc123'.encode('utf8'))  # 客户端给服务器端发送消息

    client.close()


if __name__ == '__main__':
    tcp_client()
