# author: wp
# 2022年03月02日 21:50
# 完成红黑树的新增代码编写
# 红黑树的插入操作核心点：解决双红缺陷

# 定义颜色常量
RED = 0
BLACK = 1


# 定义节点类
class RedBlackTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  # 初始左右节点均为空
        self.p = None  # 当前节点的父亲
        self.color = RED  # 假定新增节点初始颜色均为红


# 左旋函数；node是要旋转的节点，tree里边有root（没敲）
def left_rotate(tree, node):
    if not node.right:
        return False
    node_right = node.right
    node_right.p = node.p
    if not node.p:  # 如果node没有父亲，node就是根，左旋后node_right成为根
        tree.root = node_right
    elif node == node.p.left:  # node是在父亲的左边
        node.p.left = node_right
    else:
        node.p.right = node_right
    if node_right.left:
        node_right.left.p = node
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


# 右旋函数
def right_rotate(tree, node):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    if not node.p:  # 如果node没有父亲，node就是根，右旋后node_left成为根
        tree.root = node_left
    elif node == node.p.left:  # node是在父亲的左边
        node.p.left = node_left
    else:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node


class RedBlackTree:
    def __init__(self):
        self.root = RedBlackTreeNode(None)  # 添加类注释

    # 先依照二叉查找树的方法插入节点并将其标记为红色
    def insert(self, node: RedBlackTreeNode):
        if not self.root.value:
            self.root = node
        else:
            x = self.root
            y = self.root  # 辅助变量
            while x:
                y = x  # 这一设置的作用：记录最后一个判断节点；此句为这段代码核心
                if node.value > x.value:
                    x = x.right
                else:
                    x = x.left
            node.p = y
            if node.value > y.value:
                y.right = node
            else:
                y.left = node

        self.insert_fixup(node)

    def insert_fixup(self, node):
        parent: RedBlackTreeNode = node.p
        # 情形1和2无需调整，只需要将新节点插入到相应位置即可
        # 父节点存在且为红色时才需要调整（双红缺陷） 额，好像没有假想中那么困难
        while parent and parent.color == RED:
            # 定义祖父节点
            grandpa: RedBlackTreeNode = parent.p  # 有可能不存在吗？不，一定是存在的
            if parent == grandpa.left:
                uncle: RedBlackTreeNode = grandpa.right

                # 判断情形3
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandpa.color = RED
                    self.insert_fixup(grandpa)
                    break

                # 判断情形4
                if parent.right == node:
                    left_rotate(self, parent)  # 这里变量tree的位置填self
                    node, parent = parent, node

                # 判断情形5
                right_rotate(self, grandpa)
                parent.color = BLACK
                grandpa.color = RED

            else:
                uncle: RedBlackTreeNode = grandpa.left

                # 判断情形3
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandpa.color = RED
                    self.insert_fixup(grandpa)
                    break

                # 判断情形4
                if parent.left == node:
                    right_rotate(self, parent)  # 这里变量tree的位置填self
                    node, parent = parent, node

                # 判断情形5
                left_rotate(self, grandpa)
                parent.color = BLACK
                grandpa.color = RED

        self.root.color = BLACK


def rbtree_print(node, key, direction):
    if node:
        if direction == 0:  # node是根节点
            print("%2d(B) is root" % node.value)
        else:  # node是分支节点
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")))

        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3, 10)
    tree = RedBlackTree()
    for num in number_list:
        node = RedBlackTreeNode(num)
        tree.insert(node)
    rbtree_print(tree.root, tree.root.value, 0)


if __name__ == '__main__':
    main()
