import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
visited = [False]*n


# 순서 상관 없이 한번 나온 조합은 안나오게 순열을 출력해보자
def backtracking(arr, cnt, n, m):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i+1)
        backtracking(arr, cnt+1, n, m)
        for j in range(i+1, n):
            visited[j] = False
        arr.pop()


backtracking(arr, 0, n, m)
