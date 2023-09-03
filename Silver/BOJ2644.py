def dfs(x,cnt):
    cnt+=1
    visited[x]=1
    if x==y:
        result.append(cnt)
        return
    for i in lst[x]:
        if visited[i]==0:
            dfs(i,cnt)

    return -1
n = int(input())
x,y =map(int,input().split())
m = int(input())
lst = [[] for _ in range(n+1)]
result = []
visited  = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

cnt = 0
dfs(x,0)

if len(result)==0:
    print(-1)
else:
    print(result[0]-1)
