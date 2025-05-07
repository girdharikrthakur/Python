# Queue
# FIFI (First In First Out)
# ie:
# [1 ,2 ,3]
# [2,3]

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

if not queue:
    print("Empty")
