import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    k=int(input())
    n=int(input())
    
    li=[k for k in range(1,n+1)]
    
    #print(li)
    for j in range(k):
        for l in range(1,n):
            li[l]+=li[l-1]
    print(li[-1])