# 使用Python的队列deque
from collections import deque

# 增删查改
queue = deque(["Eric", "John", "Michael"])
queue.append('hello')
print(queue)
print(queue.popleft())
print(queue)

queue[0] = 'xiong da'
print(queue[0])
queue.insert(0, 'xiong er')
print(queue)
