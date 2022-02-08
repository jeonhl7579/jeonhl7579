import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    line=input().rstrip()
    
    stack=[]
    status=True
    for i in line:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==')':
            if not stack or stack[-1] != '(':
                status=False
                break
            else:
                stack.pop()
        elif i==']':
            if not stack or stack[-1] != '[':
                status=False
                break
            else:
                stack.pop()
    #print(status)
    if status==True and not stack:
        print('YES')
    else:
        print('NO')