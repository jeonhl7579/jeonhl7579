import sys
input=sys.stdin.readline

while True:
    n=int(input())
    
    if n==0:
        break
    else:
        cmp_num=str(n)
        rn=str(n)[::-1]
        
        if cmp_num == rn:
            print('yes')
        else:
            print("no")        
        