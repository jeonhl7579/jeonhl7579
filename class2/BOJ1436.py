import sys
input=sys.stdin.readline

N=int(input())

idx=0
num=1
while True:  
    str_num=str(num)
    if '666' in str_num:
        idx+=1
        if idx==N:
            break
    num+=1
    
print(num)
    