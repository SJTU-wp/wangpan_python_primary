# 完成二叉树的层次建树，并实现前序遍历，中序遍历，后序遍历
class Node:
    """定义节点类"""
    def __init__(self, node=-1, lchild=None, rchild=None):  # 缺省参数
        self.node = node
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """定义树类"""
    def __init__(self, root=None):
        self.root = root
        self.queue = []  # 辅助队列，差点忘记定义

    # 给树添加节点
    def add_node(self, node):
        new_node = Node(node)  # 对新结点进行初始化
        self.queue.append(new_node)  # 放入队列，写到后面才发现如果不定义队列的话就无法定位后续根了
        # 节点未完全前都在此辅助队列中
        if self.root is None:
            self.root = new_node  # 树为空，new_node就是树根
        elif self.queue[0].lchild is None:  # 队列[0]永远是待加节点的根
            self.queue[0].lchild = new_node
        elif self.queue[0].rchild is None:
            self.queue[0].rchild = new_node
            self.queue.pop(0)  # 此根已完全，出队

    # 前序遍历（递归）
    def preorder(self, current_node: Node):
        if current_node:
            print(current_node.node, end=' ')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    # 中序遍历（递归）
    def midorder(self, current_node: Node):
        if current_node:
            self.midorder(current_node.lchild)
            print(current_node.node, end=' ')
            self.midorder(current_node.rchild)

    # 后序遍历（递归）
    def postorder(self, current_node: Node):
        if current_node:
            self.postorder(current_node.lchild)
            self.postorder(current_node.rchild)
            print(current_node.node, end=' ')


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add_node(i)
    tree.preorder(tree.root)
    print()
    tree.midorder(tree.root)
    print()
    tree.postorder(tree.root)
