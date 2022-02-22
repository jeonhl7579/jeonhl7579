import sys
input=sys.stdin.readline

m,n=map(int,input().split())

def prime_list(n):
    sieve=[True]*n
    
    m=int(n**0.5)
    
    for i in range(2,m+1):
        if sieve[i]==True:
            for j in range(i+i,n,i):
                sieve[j]=False

    return [i for i in range(2,n) if sieve[i]==True]

result=prime_list(n+1)

#print(result)
for i in result:
    if i < m:   
        continue
    print(i)