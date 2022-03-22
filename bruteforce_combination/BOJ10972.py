import sys
from itertools import permutations
input = sys.stdin.readline


# 런타임 에러 : 재귀 깊이로 인해서 오류 뜸

# n = int(input())
# arr = list(map(int, input().split()))
# # 1부터 n까지의 숫자 리스트
# numlist = [i for i in range(1, n+1)]
# # 방문 리스트
# visited = [False]*n
# # 결과 저장소
# result = []
# # 중간 저장소
# li = []


# def solve(cnt):
#     if cnt == n:
#         result.append(li[:])
#         return

#     for i in range(n):
#         if visited[i]:
#             continue

#         visited[i] = True
#         li.append(numlist[i])
#         solve(cnt+1)
#         li.pop()
#         visited[i] = False


# solve(0)

# if result[-1] == arr:
#     print(-1)
# else:
#     print(*result[result.index(arr)+1])

# itertools를 이용한 순열 조합으로 문제를 해결해보자.

n = int(input())
arr = list(map(int, input().split()))
numlist = [i for i in range(1, n+1)]
result = []
for i in permutations(numlist, n):
    result.append(list(i))

if result[-1]==arr:
    print(-1)
else:
    print(*result[result.index(arr)+1])
