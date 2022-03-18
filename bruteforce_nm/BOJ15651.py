import sys
input = sys.stdin.readline


def backtracking(arr, cnt, n, m):
    if cnt == m:
        print(*arr)
        return

    for i in range(1, n+1):
        arr.append(i)
        backtracking(arr, cnt+1, n, m)
        arr.pop()


n, m = map(int, input().split())
arr = []
backtracking(arr, 0, n, m)
