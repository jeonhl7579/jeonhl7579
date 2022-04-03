import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
sea = []
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(n):
    sea.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            queue.append([i, j])

# 처음에는 인자값을 받아들이고 함수를 작성하였으나, 그렇게 되면 입력받은 값을 기준으로만 안전거리를
# 계산하게 되므로 1인 값들을 queue에 저장해놓는 방식으로 바꿨다.


def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            na = a+dy[i]
            nb = b+dx[i]
            if na < 0 or na >= n or nb < 0 or nb >= m:
                continue
            if sea[na][nb] == 0:
                sea[na][nb] = sea[a][b]+1
                queue.append([na, nb])
    return


bfs()
max_num = 0
for i in range(n):
    for j in range(m):
        max_num = max(max_num, sea[i][j])

print(max_num-1)
