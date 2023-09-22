n,m = map(int,input().split())
start,end = 0,1
lst = list(map(int,input().split()))

cnt = 0
while 1:
    Sum = 0
    for i in range(start,end):
        Sum+=lst[i]
    if Sum==m:
        cnt+=1
        start+=1
    elif Sum<m:
        end+=1
    elif Sum>m:
        start+=1
    if end>n:
        break

print(cnt)