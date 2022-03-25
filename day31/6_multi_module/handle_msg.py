# author: wp
# 2022年03月21日 21:38
from common import RECV_DATA_LIST
from common import HANDLE_FLAG  # 这种方式导入 HANDLE_FLAG修改后，其他模块不感知
# import common


def handle_data():
    """模拟处理recv_msg模块接收的数据"""
    print("--->handle_data")
    for i in RECV_DATA_LIST:
        print(i)

    # 既然处理完成了，那么将变量HANDLE_FLAG设置为True，意味着处理完成
    global HANDLE_FLAG  # 这里直接会警告的原因是？
    # 与上面导入部分的灰色对应着看 说明此变量相当于是在当前模块中的一个新的变量 其他模块中的修改影响不到它（独立了）
    HANDLE_FLAG = True
    # common.HANDLE_FLAG = True


def test_handle_data():
    """测试处理是否完成，变量是否设置为True"""
    print("--->test_handle_data")
    # if common.HANDLE_FLAG:
    if HANDLE_FLAG:
        print("=====已经处理完成====")
    else:
        print("=====未处理完成====")
