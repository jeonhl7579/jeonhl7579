import sys

input=sys.stdin.readline

N=int(input())

for i in range(1,N+1): 
    str_num=str(i)
    result=i
    for j in str_num:
        result+=int(j)
    if result==N:
        print(i)
        break
    
    if i==N:
        print(0)