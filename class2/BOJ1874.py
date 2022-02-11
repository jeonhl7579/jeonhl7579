import sys
input=sys.stdin.readline

n=int(input())
arr=[]

stack=[]
status=True
cnt=1
result=[]
for i in range(0,n):
    a=int(input())
    
    while cnt<=a:
        stack.append(cnt)
        cnt+=1
        result.append('+')
    if stack[-1]==a:
        stack.pop()
        result.append("-")
    else:
        status=False
        break
        
if status==False:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])
    