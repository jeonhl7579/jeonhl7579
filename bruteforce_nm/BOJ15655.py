import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False]*n
li = []


def backtracking(cnt):
    if cnt == m:
        print(*li)
        return

    for i in range(len(arr)):
        if visited[i]:
            continue

        visited[i] = True
        li.append(arr[i])
        backtracking(cnt+1)

        for j in range(i+1, n):
            visited[j] = False
        li.pop()


# print(arr)
backtracking(0)
