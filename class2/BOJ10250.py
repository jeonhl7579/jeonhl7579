import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    H,W,N=map(int,input().split())
    
    if N%H==0:
        floor=H
        room=N//H
    else:
        floor=N%H
        room=(N//H)+1
    print(floor*100+room)