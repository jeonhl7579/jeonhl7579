import sys
input=sys.stdin.readline

def push(stack,x):
    stack.append(x)
    return stack

def pop(stack):
    if not stack:
        return -1
    else:
        return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    if stack:
        return 0
    else:
        return 1
    
def top(stack):
    if not stack:
        return -1
    else:
        return stack[-1]
    
    
n=int(input())
stack=[]

for i in range(n):
    a=input().split()
    #print(a)
    if len(a)==2:
        if a[0] == 'push':
            push(stack,a[1])
    elif len(a)==1:
        if a[0] == 'pop':
            print(pop(stack))
        elif a[0] =='size':
            print(size(stack))
        elif a[0] == 'empty':
            print(empty(stack))
        elif a[0] == 'top':
            print(top(stack))