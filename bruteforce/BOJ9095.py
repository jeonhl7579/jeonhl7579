import sys
input = sys.stdin.readline


t = int(input())


# 다이나믹 프로그래밍은 이전에 구했던 값들을 저장해놓고 일일히 재계산 하지 않는방법
# 재귀 함수가 이에 사용 가능한듯
def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return solve(n-1)+solve(n-2)+solve(n-3)


for i in range(t):
    num = int(input())
    print(solve(num))
