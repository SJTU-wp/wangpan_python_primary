# 实现目录深度优先遍历

import os


def dir_dfs(path, width):
    file_list = os.listdir(path)
    for filename in file_list:  # 遍历当前目录下的所有文件
        print(' ' * width + filename)
        if os.path.isdir(path + '/' + filename):  # 如果是目录
            dir_dfs(path + '/' + filename, width + 4)


if __name__ == '__main__':
    # os.mkdir('./dir1/dir4')
    # os.mkdir('./dir1/dir5')
    # os.mkdir('./dir1/dir4/dir6')
    # os.mkdir('./dir1/dir5/dir7')
    dir_dfs('./dir1', 0)
