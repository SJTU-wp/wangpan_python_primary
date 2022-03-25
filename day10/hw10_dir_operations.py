# 创建文件夹，删除文件夹（均使用相对路径），改变程序执行路径，获取程序当前路径

import os

os.mkdir('dir1')
os.mkdir('dir2')
os.mkdir('dir3')
os.mkdir('dir_del')
os.rmdir('dir_del')
print(os.getcwd())
os.chdir('./dir1')
print(os.getcwd())
