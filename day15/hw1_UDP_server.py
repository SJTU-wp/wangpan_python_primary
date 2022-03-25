# author: wp
# 2022年03月03日 12:25
# 完成UDP服务器端代码编写

import socket

# 创建udp服务器端的套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ('192.168.5.9', 2000)   # 写1024以上端口
s.bind(addr)  # 绑定，失败则直接抛出异常

data, client_addr = s.recvfrom(100)  # 100代表接的长度
print(data.decode('utf8'))  # 当client发送给server字节流时，需要解码
print(client_addr)

s.sendto('你太棒了'.encode('utf8'), client_addr)

# 不用的时候，关闭套接字
s.close()
