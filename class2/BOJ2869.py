import sys
input=sys.stdin.readline

A,B,V=map(int,input().split())

result=(V-B)/(A-B)
print(result)
if result == int(result):
    print(int(result))
else:
    print(int(result)+1)