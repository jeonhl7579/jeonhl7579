import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book = []
for i in range(n):
    book.append(input().rstrip())
    #book[str(i)] = input().rstrip()

# print(book)

for i in range(m):
    ans = input().rstrip()
    if ans.isdigit():
        print(book[int(ans)-1])
    else:
        print(book.index(ans)+1)
