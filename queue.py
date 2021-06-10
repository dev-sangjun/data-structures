from collections import deque

queue = deque()

queue.append(1)
queue.append(3)

# peek
print(queue[0])

print(queue.popleft())
print(queue.popleft())