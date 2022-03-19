import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

result = p[:]
for i in range(n):
    if i+t[i] > n:
        result[i] = 0
        continue

    for j in range(i+t[i], n):
        #print(i, i+t[i], result[i], p[j])
        if result[i]+p[j] > result[j]:
            result[j] = result[i]+p[j]


print(max(result))
