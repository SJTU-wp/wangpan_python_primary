# 实现有5个元素的循环队列


class CircularQueue:
    # 初始化队列
    def __init__(self, maxsize):
        self.queue = [None] * maxsize  # 用deque之后append或pop时都会让改变占用空间
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    # 如果队列未满，则在队尾入队元素
    def in_queue(self, data):
        if (self.rear + 1) % self.maxsize == self.front:
            print("队列已满，无法入队！")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.maxsize
            # self.rear += 1  # 当rear=5时，溢出了，必须再次从0开始

    # 如果队列非空，则在队首出队元素
    def out_queue(self):
        if self.front == self.rear:
            print("队列为空，无法出队！")
        else:
            print(self.queue[self.front])
            self.queue[self.front] = None
            # 钟：出队时不需要把front设为None的，系统会自动在该位置保留原来的数据，但不会再次被读了，等到下一轮入队时会被新数据覆盖掉
            self.front = (self.front + 1) % self.maxsize
            # self.front += 1


if __name__ == '__main__':
    circular_queue = CircularQueue(5)
    for i in range(3, 7):
        circular_queue.in_queue(i)
    print(circular_queue.queue)

    circular_queue.in_queue(7)
    circular_queue.out_queue()
    circular_queue.out_queue()
    circular_queue.in_queue(8)
    circular_queue.in_queue(9)
    print(circular_queue.queue)

    for i in range(4):
        circular_queue.out_queue()
    print(circular_queue.queue)
    circular_queue.out_queue()
