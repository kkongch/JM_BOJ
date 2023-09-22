import sys

input = sys.stdin.readline
n,k = map(int,input().split())
lst = list(map(int,input().split()))
end = 0
# result = []
Max = 0
limit,cnt=0,0
for start in range(n):
    while limit<=k and end<n:
        if lst[end]%2:
            limit+=1
        else:
            cnt+=1
        end+=1
    if Max<cnt:
        Max = cnt
    if lst[start]%2:
        limit-=1
    else:
        cnt-=1



print(Max)