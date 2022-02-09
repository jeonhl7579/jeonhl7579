import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())

queue=deque([i for i in range(1,n+1)])

cnt=0
print('<',end='')
while True:
    if not queue:
        break
    if cnt==k-1:
        print(queue.popleft(),end='')
        if len(queue)==0:
           break
        else:
           print(',',end=' ')
        cnt=0
        continue
    #print(queue)
    queue.append(queue.popleft())
    cnt+=1

#print(result)
print('>')
