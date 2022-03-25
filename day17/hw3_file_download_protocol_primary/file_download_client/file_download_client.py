# author: wp
# 2022年03月06日 22:13

from socket import *
import struct

c = socket(AF_INET, SOCK_STREAM)
addr = ('192.168.5.9', 2000)
c.connect(addr)

# 先读4个字节的火车头，接收文件名
train_head_bytes = c.recv(4)
train_content_len = struct.unpack('I', train_head_bytes)
file_name = c.recv(train_content_len[0])
f = open(file_name.decode('utf8'), 'wb')

# 先读4个字节的火车头，接收文件内容
train_head_bytes = c.recv(4)
train_content_len = struct.unpack('I', train_head_bytes)
f_content = c.recv(train_content_len[0])
f.write(f_content)  # 写入，对应15行的'wb'

f.close()
c.close()
