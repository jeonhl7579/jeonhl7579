import sys
input=sys.stdin.readline

while True:
    fellin=input().rstrip()
    value=True
    if fellin=='0':
        break
    else:
        res_fellin=fellin[::-1]
        
        if fellin==res_fellin:
            print('yes')
        else:
            print('no')