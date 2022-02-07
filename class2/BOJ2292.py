import sys

input=sys.stdin.readline
house=1
n=int(input())
idx=1
while n>house:
    house+=(6*idx)
    idx+=1
    
print(idx)
    