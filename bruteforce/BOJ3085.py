import sys
input = sys.stdin.readline
n = int(input())
maxCnt = 1

board = []

for i in range(n):
    board.append(list(input().rstrip()))


def search():
    global maxCnt

    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1


for i in range(n):
    for j in range(n-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        search()
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

for i in range(n):
    for j in range(n-1):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        search()
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]


print(maxCnt)
