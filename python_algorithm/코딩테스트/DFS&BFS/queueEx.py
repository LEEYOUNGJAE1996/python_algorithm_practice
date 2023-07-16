# 230716

# deque 라이브러리를 사용

from collections import deque

queue = deque()

queue.append(10)
print(queue)
print(queue.popleft())

# 직접 구현해보기 
queueSelf = []
count = 0
def queuePush(queue, data, count):
    count += 1
    queue.append(data) 
    return queue, count
def queuePop(queue, count):
    if count <= 0:
        return queue, None, count 
    else :
        data = queue.pop(0)
        count -= 1 
        return queue, data, count
    
queueSelf, count = queuePush(queue=queueSelf,data = 10, count =count)
print(queueSelf)
queueSelf, data, count = queuePop(queue=queueSelf, count=count)
print(queueSelf, data)
queueSelf, data, count = queuePop(queue=queueSelf, count=count)
print(queueSelf, data)