import sys
input = sys.stdin.readline


def backtracking(arr, visited, cnt, n, m):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i]:
            continue

        # 지나온 부분은 모두 true
        for j in range(i):
            visited[j] = True

        arr.append(i+1)
        backtracking(arr, visited, cnt+1, n, m)
        arr.pop()
        for a in range(i+1, n):
            visited[a] = False
        #visited[i] = True


n, m = map(int, input().split())
arr = []
visited = [False]*n
backtracking(arr, visited, 0, n, m)
