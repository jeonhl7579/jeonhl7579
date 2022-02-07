import sys
input=sys.stdin.readline

N=int(input())

number=[0]*10001

for i in range(N):
    n=int(input())
    number[n]+=1

for i in range(10001):
    if number[i] != 0:
        for j in range(number[i]):
            print(i)