import sys
input = sys.stdin.readline

# 시간 초과
# n = int(input())
# line = ''

# for i in range(1, n+1):
#     line += str(i)


# print(len(line))

n = int(input())
ln = len(str(n))-1
i = 0
cnt = 0
while ln > i:
    cnt += 9*(10**i)*(i+1)
    i += 1

cnt += ((n-(10**ln))+1)*(ln+1)
print(cnt)
