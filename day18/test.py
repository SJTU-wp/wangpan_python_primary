# author: wp
# 2022年03月06日 23:00
import struct

a = 'eaesds'.encode('utf8')
print(a)
print(struct.pack('p', a))
