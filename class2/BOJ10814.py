import sys
input=sys.stdin.readline

N=int(input())
member=[]

for i in range(N):
    age,name=input().split()
    member.append([int(age),name])
    
#print(member)

member=sorted(member,key=lambda x:x[0])

for i in range(len(member)):
    print(*member[i])
