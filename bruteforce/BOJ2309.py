import sys
input = sys.stdin.readline

# input => 9개의 난쟁이 키, output => 키의 합이 100

key = []
for i in range(9):
    key.append(int(input()))

# 더하는 것을 기준으로 반복문을 작성하면 반복문이 많이 필요하므로
# 빼는 것을 기준으로 생각해보자.

# 아홉명의 키를 모두 더하자
sum_key = sum(key)

# 그 이후 두 난쟁이으 키의 합을 뺐을 때의 합이 100이 나오면 된다.

for i in range(9):
    for j in range(i+1, 9):
        if sum_key-key[i]-key[j] == 100:
            ra = key[i]
            rb = key[j]

# 찾은 값들을 제거
key.remove(ra)
key.remove(rb)
# 정렬
key.sort()

for i in range(len(key)):
    print(key[i])
