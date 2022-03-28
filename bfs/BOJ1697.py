import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
distance = [0]*100001


def bfs():
    q = deque()
    q.append(n)
    while q:
        a = q.popleft()
        if a == k:
            print(distance[a])
            break
        for case in (a-1, a+1, a*2):
            if 0 <= case <= 100000 and not distance[case]:
                distance[case] = distance[a]+1
                q.append(case)


bfs()
