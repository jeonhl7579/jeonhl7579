import sys
input=sys.stdin.readline

k=int(input())
result=[]
for i in range(k):
    n=int(input())
    if n != 0:
        result.append(n)
    else:
        result.pop()
        
print(sum(result))