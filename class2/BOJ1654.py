import sys
input=sys.stdin.readline


k,n=map(int,input().split())
arr=[]
for i in range(k):
    arr.append(int(input()))
    
# 이분 탐색 느낌으로다가
start,end=1,max(arr)

while start<=end:
    mid=(start+end)//2
    
    cnt=0
    for i in arr:
        cnt+=i//mid
    if cnt>=n:
        start=mid+1
    else:
        end=mid-1
        
print(end)