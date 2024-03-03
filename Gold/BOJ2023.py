n = int(input())
lst = list(map(int,input().split()))
start,end = 0,1
lst.sort()
cnt = 0
ans = []
while 1:
    if end == n:
        start +=1
        if start == end-1:
            break
        end = start+1
    if (lst[start]+lst[end]) in lst:
        ans.append(lst.index(lst[start]+lst[end]))
    end+=1
print(ans)
print(len(set(ans)))