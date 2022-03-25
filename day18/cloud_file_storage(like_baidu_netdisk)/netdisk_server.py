# author: wp
# 2022年03月05日 10:59
from socket import *
import struct
import os


class Server:
    def __init__(self, ip, port):
        self.s = None
        self.ip = ip
        self.port = port

    def tcp_init(self):
        self.s: socket = socket(AF_INET, SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.s.listen(128)

    def task(self):
        new_client, client_addr = self.s.accept()
        user = User(new_client)
        user.deal_command()  # 处理客户端发过来的各种命令


class User:
    """每一个user对象对应一个客户端"""

    def __init__(self, new_client: socket):
        self.new_client = new_client
        self.user_name = None
        self.path = os.getcwd()  # 存储连上的用户的路径

    def deal_command(self):
        while True:
            command = self.recv_train().decode('utf8')
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd(command)
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm(command)
            elif command[:4] == 'gets':
                self.do_gets(command)
            elif command[:4] == 'puts':
                self.do_puts(command)
            else:
                print('wrong command')

    def send_train(self, send_bytes):
        """send火车：把某个字节流的内容以火车形式发过去"""
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.new_client.send(train_head_bytes + send_bytes)

    def recv_train(self):
        """recv火车：接收以火车形式发送过来的字节流，并返回所携带的内容"""
        train_head_bytes = self.new_client.recv(4)
        train_head = struct.unpack('I', train_head_bytes)
        return self.new_client.recv(train_head[0])

    def do_ls(self):
        """当前路径下的信息传输给客户端，模仿Linux下的ls命令"""
        data = ''
        for file in os.listdir(self.path):  # 遍历，得到数据，发送给客户端，再由客户端打印输出
            data = data + file + ' ' * 5 + str(os.stat(file).st_size) + '\n'  # 连同大小一并显示
        self.send_train(data.encode('utf8'))

    def do_cd(self, command):
        """切换路径"""
        path = command.split()[1]  # 记录要切换到的路径
        os.chdir(path)  # 直接简单粗暴
        self.path = os.getcwd()  # 更新self.path
        self.send_train(self.path.encode('utf8'))

    def do_pwd(self):
        """显示当前在服务器上的路径"""
        self.send_train(self.path.encode('utf8'))

    def do_rm(self, command):
        """删除文件"""
        path = command.split()[1]
        os.remove(path)
        data = '%s removed' % path
        self.send_train(data.encode('utf8'))

    def do_gets(self, command):
        """下载文件"""
        filename = command.split()[1]  # 前提是文件名不能有空格
        filename_bytes = filename.encode('utf8')
        self.send_file_name(filename_bytes)
        self.send_file_content(filename)

    def do_puts(self, command):
        """上传文件"""
        pass

    def send_file_name(self, filename_bytes):
        """发送文件名"""
        self.send_train(filename_bytes)

    def send_file_content(self, filename):
        """发送文件内容"""
        try:
            with open(filename, 'rb') as f:
                file_content_bytes = f.read()
                if file_content_bytes:
                    f.close()
                    return self.send_train(file_content_bytes)
        except:
            print("没有要下载的文件 %s" % filename)

    def recv_file_name(self):
        """接收文件名"""
        pass

    def recv_file_content(self):
        """接收文件内容"""
        pass


if __name__ == '__main__':
    s = Server('', 2000)
    s.tcp_init()
    s.task()
