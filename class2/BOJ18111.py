import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())

field=[list(map(int,input().split())) for _ in range(n)]
    
# 목표 높이를 0부터 256일 때를 기준으로 계산
height=0
result=1000000000000000000000000000000

for i in range(257):
    max=0
    min=0
    for a in range(n):
        for b in range(m):
            if field[a][b] < i:
                min += (i-field[a][b])
            else:
                max += (field[a][b]-i)
    inven=max+b

    # 설치해야 되는블럭의 갯수가 인벤에 있는 블럭의 갯수보다 작으면 넘어가기
    if inven >= min:
    # max는 2초 , min은 1초
        time=2*max+min
        if time <= result:
            result=time
            height=i
        
print(result,height)