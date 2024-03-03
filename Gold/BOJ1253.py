
n = int(input())
lst = list(map(int,input().split()))

lst.sort()
cnt = 0

for i in range(n):
    start,end = 0,len(lst)-1
    target = lst[i]
    while start<end:
        if lst[start]+lst[end]==target:
            if start==i:
                start+=1
            elif end == i:
                end -=1
            else:
                cnt+=1
                break
        elif lst[start]+lst[end]>target:
            end-=1
        elif lst[start]+lst[end]<target:
            start+=1

print(cnt)