import sys
input=sys.stdin.readline

N=int(input())

physical=[]
for i in range(N):
    x,y=map(int,input().split())
    physical.append([x,y])

rank=[]
for i in range(len(physical)):
    cnt=1
    for j in range(len(physical)):
        # 자기 자신은 제외
        if i==j:
            continue
        if physical[i][0] < physical[j][0] and physical[i][1] < physical[j][1]:
            cnt+=1
    rank.append(cnt)
    
print(*rank)