import sys
input=sys.stdin.readline

# input = 두 개의 자연수
# output = 최대 공약수, 최소 공배수

a,b=map(int,input().split())

ca,cb=a,b
while True:
    r=ca%cb
    if ca%cb==0:
        break
    ca=cb
    cb=r
    
print(cb)
print(int((a/cb)*(b/cb)*cb))