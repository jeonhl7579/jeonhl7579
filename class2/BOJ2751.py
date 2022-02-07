import sys
input=sys.stdin.readline

N=int(input())
num_list=[]

for i in range(N):
    number=int(input())
    num_list.append(number)
    
num_list=sorted(num_list,key=lambda x:x)

for i in range(len(num_list)):
    print(num_list[i])
    
    