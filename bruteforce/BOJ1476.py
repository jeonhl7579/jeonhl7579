import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
te, ts, tm = 1, 1, 1
idx = 1
while True:
    # 조건
    if te == e and ts == s and tm == m:
        break
    te += 1
    ts += 1
    tm += 1
    idx += 1
    if te > 15:
        te -= 15
    if ts > 28:
        ts -= 28
    if tm > 19:
        tm -= 19


print(idx)
