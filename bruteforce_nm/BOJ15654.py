import sys
input = sys.stdin.readline


def backtracking(arr, visited, result, cnt, n, m):
    if cnt == m:
        print(*result)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        result.append(arr[i])
        backtracking(arr, visited, result, cnt+1, n, m)
        result.pop()
        visited[i] = False

    return


n, m = map(int, input().split())
arr = list(map(int, input().split()))
sarr = sorted(arr)
result = []
visited = [False]*n

backtracking(sarr, visited, result, 0, n, m)
