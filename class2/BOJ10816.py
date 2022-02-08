import sys
input=sys.stdin.readline

N=int(input())
ncard=list(map(int,input().split()))
ncard=sorted(ncard)
M=int(input())
mcard=list(map(int,input().split()))

def solution(tmp,num):
    left=0
    right=len(tmp)-1
    
    while (left<=right):
        mid=(left+right)//2
        if tmp[mid]==num:
            return tmp[left:right+1].count(num)
        elif tmp[mid]<num:
            left=mid+1
        elif tmp[mid] > num:
            right=mid-1
            
    return 0

#print(solution(ncard,mcard[0]))  
# result=[]
# for i in range(M):
#     search=mcard[i]
#     length=N
#     center=length//2
#     while True:
#         if ncard[center] == search:
    
ndic={}        
for i in mcard:
    if i not in ndic:
        ndic[i]=solution(ncard,i)

print(' '.join(str(ndic[x]) if x in ndic else '0' for x in mcard))