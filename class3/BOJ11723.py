import sys
input = sys.stdin.readline


m = int(input())
s = set()

for _ in range(m):
    a = input().split()
    if len(a) == 1:
        element = a[0]
        if element == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        element = a[0]
        target = int(a[1])
        if element == "add":
            s.add(target)
        elif element == "remove":
            # remove보다는 discard를 사용해야 한다.
            # remove는 집합내에 삭제하려는 요소가 없는 순간 KeyError를 반환하는데
            # discard는 없어도 결과를 반환해준다.
            s.discard(target)
        elif element == "check":
            if target in s:
                print(1)
            else:
                print(0)
        elif element == "toggle":
            if target in s:
                s.discard(target)
            else:
                s.add(target)
