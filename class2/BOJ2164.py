import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
queue=deque()
for i in range(1,N+1):
    queue.append(i)
#print(len(queue))
#print(card)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])



