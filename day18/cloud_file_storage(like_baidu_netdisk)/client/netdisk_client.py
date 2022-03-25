# author: wp
# 2022年03月05日 11:01
from socket import *
import struct
import os


class Client:
    def __init__(self, ip, port):
        self.client = None
        self.ip = ip
        self.port = port
        self.path = os.getcwd()

    def tcp_connect(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.ip, self.port))

    def send_train(self, send_bytes):
        """send火车：把某个字节流的内容以火车形式发过去"""
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.client.send(train_head_bytes + send_bytes)

    def recv_train(self):
        """recv火车：接收以火车形式发送过来的字节流，并返回所携带的内容"""
        train_head_bytes = self.client.recv(4)
        train_head = struct.unpack('I', train_head_bytes)
        return self.client.recv(train_head[0])

    def send_command(self):
        """发送各种命令给服务器"""
        while True:
            command = input()  # 输入命令
            self.send_train(command.encode('utf8'))  # 以字节流形式发送到服务器端，s端再解码
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd()
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm()
            elif command[:4] == 'gets':
                self.do_gets()
            elif command[:4] == 'puts':
                self.do_puts(command)
            else:
                print('wrong command')

    def do_ls(self):  # 客户端这些方法的作用：接收结果（相当于你输入这些命令会得到怎样的显示结果）
        """接收服务器端传来的当前路径下的信息"""
        data = self.recv_train().decode('utf8')
        print(data)

    def do_cd(self):  # 仅支持三种情况：.. dir1 绝对路径
        """接收路径切换结果"""
        print(self.recv_train().decode('utf8'))

    def do_pwd(self):
        """接收当前工作目录信息"""
        print(self.recv_train().decode('utf8'))

    def do_rm(self):
        """删除文件"""
        print(self.recv_train().decode('utf8'))

    def do_gets(self):
        """下载文件"""
        filename = self.recv_file_name()
        self.recv_file_content(filename)

    def do_puts(self, command):
        """上传文件"""
        pass

    def recv_file_name(self):
        """接收文件名"""
        return self.recv_train().decode('utf8')

    def recv_file_content(self, filename):
        """接收文件内容"""
        with open(self.path + '/' + filename, 'wb') as f:
            f.write(self.recv_train())
            f.close()


if __name__ == '__main__':
    client = Client('192.168.5.9', 2000)
    client.tcp_connect()
    client.send_command()
