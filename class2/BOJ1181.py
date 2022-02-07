import sys
input=sys.stdin.readline

N=int(input())
word_list=[]
for i in range(N):
    tmp=input().rstrip()
    word_list.append(tmp)
    
word_list=list(set(word_list))

word_list=sorted(word_list,key=lambda x: (len(x),x))

for i in range(len(word_list)):
    print(word_list[i])