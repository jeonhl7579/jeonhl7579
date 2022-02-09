import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

def push_front(queue,x):
    return queue.appendleft(x)

def push_back(queue,x):
    return queue.append(x)

def pop_front(queue):
    if not queue:
        return -1
    else:
        return queue.popleft()

def pop_back(queue):
    if not queue:
        return -1
    else:
        return queue.pop()
    
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
        if a[0] == 'push_back':
            push_back(queue,int(a[1]))
    if a[0] == 'push_front':
        push_front(queue,int(a[1]))
    elif len(a)==1:
        if a[0] == "pop_front":
            print(pop_front(queue))
        elif a[0] == "pop_back":
            print(pop_back(queue))
        elif a[0] == "size":
            print(size(queue))
        elif a[0] == "empty":
            print(empty(queue))
        elif a[0] == "front":
            print(front(queue))
        elif a[0] == "back":
            print(back(queue))
        
        
        

