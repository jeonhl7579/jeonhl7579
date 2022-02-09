import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

def push(queue,x):
    return queue.append(x)
    
def pop(queue):
    if not queue:
        return -1
    else:
        return queue.popleft()

def size(queue):
    return len(queue)

def empty(queue):
    if queue:
        return 0
    else:
        return 1
    
def front(queue):
    if queue:
        return queue[0]
    else:
        return -1

def back(queue):
    if queue:
        return queue[-1]
    else:
        return -1
    
queue=deque()
for i in range(n):
    a=input().split()
    if len(a)==2:
        if a[0] == 'push':
            push(queue,int(a[1]))
    elif len(a)==1:
        if a[0] == "pop":
            print(pop(queue))
        elif a[0] == "size":
            print(size(queue))
        elif a[0] == "empty":
            print(empty(queue))
        elif a[0] == "front":
            print(front(queue))
        elif a[0] == "back":
            print(back(queue))
        
        
        

