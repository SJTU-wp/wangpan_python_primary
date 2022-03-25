# author: wp
# 2022年03月06日 22:13

from socket import *
import struct


def tcp_init():
    s = socket(AF_INET, SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    return s


def server_send_file():
    file_name = 'hw3_file'
    s = tcp_init()
    new_client, client_addr = s.accept()

    # 先发文件名（火车头+文件名内容）
    file_name_bytes = file_name.encode('utf8')
    train_head_bytes = struct.pack('I', len(file_name_bytes))
    new_client.send(train_head_bytes + file_name_bytes)

    # 再发文件内容（火车头+文件内容）
    f = open(file_name, 'rb')  # 只读字节流
    f_content_bytes = f.read()
    train_head_bytes = struct.pack('I', len(f_content_bytes))
    new_client.send(train_head_bytes + f_content_bytes)
    f.close()
    new_client.close()
    s.close()


if __name__ == '__main__':
    server_send_file()
