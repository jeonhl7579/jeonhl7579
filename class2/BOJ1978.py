import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
# 에라토스테네스의 체
def prime_list():
    sieve=[True]*1001
    
    # 위 문제에서 1,000이하의 자연수라는 조건이 걸려있으므로
    # sqrt(n)까지의 배수들을 지워줘야 하므로 sqrt(n)의 값을 구해준다.
    m=int(1001**0.5)
    for i in range(2,m+1):
        # 만약 sieve[i]의 값이 소수이면
        if sieve[i]==True:
            # 해당 소수의 배수들을 False 처리 해준다
            for j in range(i+i,1001,i):
                sieve[j]=False
    
    # True인 애들은 모두 소수이므로 소수들만 return
    return [i for i in range(2,1001) if sieve[i]==True]

result=prime_list()
cnt=0
for i in range(N):
    if arr[i] in result:
        cnt+=1
        
print(cnt)