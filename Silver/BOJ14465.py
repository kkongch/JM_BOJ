n,k,b = map(int,input().split())
high, low = 1,1
lst = [0]*(n+1)
result = []
for i in range(b):
    lst[int(input())] = 1
while 1:
    cnt =0
    if high-low+1 < k:
        high+=1
        continue
    for i in range(low,high+1):
        if lst[i]==1:
            cnt+=1
    if high-low+1 ==k:
        result.append(cnt)
        low+=1
    if high == n  and high-low+1<k:
        break
print(min(result))