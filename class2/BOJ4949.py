import sys
input=sys.stdin.readline

while True: 
    # 입력
    lines=input().rstrip()
    if lines=='.':
        break
    # 괄호 비교
    stack=[]
    status=True
    for i in lines:
        # 왼쪽 소괄호 일때 스택에 넣기
        if i == '(' or i=='[':
            stack.append(i)
        # 오른쪽 소괄호 일때 스택에서 빼기
        elif i == ')':
            if not stack or stack[-1]=='[':
                status=False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif i==']':
            if not stack or stack[-1]=='(':
                status=False
                break
            elif stack[-1]=='[':
                stack.pop()
    
    if status==True and not stack:
        print('yes')
    else:
        print('no')
        