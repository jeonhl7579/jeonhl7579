import operator
import sys
input=sys.stdin.readline

N=int(input())
number=[]
for i in range(N):
    a=int(input())
    number.append(a)
    
def one(arr):
    return sum(arr)//len(arr)

def two(arr):
    arr=sorted(arr)
    return arr[len(arr)//2]

def three(arr):
    max_cnt=0
    dict={}
    for i in arr:
        tmp=arr.count(i)
        if tmp > max_cnt:
            max_cnt=tmp
        if tmp in dict.keys():
            dict[tmp].append(i)
        else:
            dict[tmp]=[i]
    #print(max_cnt)
    
    result=sorted(list(set(dict[max_cnt])))
    #print(result)
    if len(result)==1:
        return result[0]
    else:
        return result[1]
    #return result
    
def four(arr):
    return max(arr)-min(arr)

print(one(number))
print(two(number))
print(three(number))
print(four(number))