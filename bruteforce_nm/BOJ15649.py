import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []


def backtracking(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if i in arr:
            continue
        arr.append(i)
        backtracking(arr, n, m)
        arr.pop()


backtracking(arr, n, m)
