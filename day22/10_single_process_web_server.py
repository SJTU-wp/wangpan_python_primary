# author: wp
# 2022年03月10日 23:46
# 单进程web服务器编写
import socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 为了确保端口复用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定
tcp_server_socket.bind(("192.168.5.9", 7890))

# 变为监听套接字
tcp_server_socket.listen(128)


new_socket, client_addr = tcp_server_socket.accept()
http_head = new_socket.recv(10000)
print(http_head.decode('utf8'))

response = "HTTP/1.1 200 OK\r\n"
response += "\r\n"
response += '<html><h1>hello world</h1></html>'

new_socket.send(response.encode('utf8'))
new_socket.close()
