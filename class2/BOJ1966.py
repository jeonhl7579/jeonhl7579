import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for i in range(t):
    queue=deque()
    n,m=map(int,input().split())
    arr=deque(map(int,input().split()))
    
    cnt=0
    while arr:
        best=max(arr)
        front=arr.popleft()
        m=m-1
        
        if best==front:
            cnt+=1
            if m<0:
                print(cnt)
                break
        else:
            arr.append(front)
            if m<0:
                m=len(arr)-1
    
