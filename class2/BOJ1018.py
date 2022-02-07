import sys
input=sys.stdin.readline


N,M=map(int,input().split())
board=[list(input().rstrip()) for i in range(N)]
result=[]

#=====================실패 코드 ======================#
for i in range(N-7):
    for j in range(M-7):
        value=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                # i,j와 a,b의 나머지 2 값이 같으면
                if ((a+b)%2) == 0:
                    if square[cmp] == board[a][b]:
                        continue
                    else:
                        value+=1
                else:
                    if square[abs(cmp-1)] == board[a][b]:
                        continue
                    else:
                        value+=1     
    result.append(value)

#=============참고해서 맞은 답 =================#

# for i in range(N-7):
#     for j in range(M-7):
#         w_idx=0
#         b_idx=0
#         for a in range(i,i+8):
#             for b in range(j,j+8):
#                 # a+b가 짝수이면
#                 if ((a+b)%2) == 0:
#                     # 짝수 
#                     if board[a][b] == "W":
#                         b_idx+=1
#                     if board[a][b] == "B":
#                         w_idx+=1
#                 else:
#                     if board[a][b] == "W":
#                         w_idx+=1
#                     if board[a][b] == "B":
#                         b_idx+=1   
         
#         result.append(min(w_idx,b_idx))

# print(min(result))