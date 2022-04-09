import sys
from collections import deque
input = sys.stdin.readline

# 이동 범위 : x-1,x+1,x*2
distance = [0]*100001
# 추적을 위한 리스트
parent = [0]*100001
n, k = map(int, input().split())
result = []


def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        a = queue.popleft()
        if a == k:
            tmp = a
            print(distance[a])
            while tmp != n:
                result.append(tmp)
                tmp = parent[tmp]
            result.append(tmp)
            break

        for i in (a-1, a+1, a*2):
            if 0 <= i < 100001 and not distance[i]:
                distance[i] = distance[a]+1
                parent[i] = a
                queue.append(i)
    return


bfs()
result.reverse()
print(*result)
