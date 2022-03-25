# author: wp
# 2022年03月03日 14:22
# 完成UDP客户端代码编写
import socket

# 创建udp客户端的套接字
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ('192.168.5.9', 2000)

client.sendto('how are you'.encode('utf8'), dest_addr)
data, server_addr = client.recvfrom(100)  # 这步有问题
print(data.decode('utf8'))
print(server_addr)

client.close()  # 关闭时端口会释放
