import sys
input=sys.stdin.readline

N,M=map(int,input().split())

card=list(map(int,input().split()))

max_result=0
for i in range(0,len(card)-2):
    for j in range(i+1,len(card)-1):
        for z in range(j+1,len(card)):
            sum_card=card[i]+card[j]+card[z]
            if sum_card <= M:
                if sum_card>max_result:
                    max_result=sum_card
            
print(max_result)