import sys
input=sys.stdin.readline

L=int(input())

en=input().rstrip()
idx=0
value=0
for i in en:
    n=ord(i)-96
    value+=n*(31**idx)
    idx+=1
    
print(value%1234567891)