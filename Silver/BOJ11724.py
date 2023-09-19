def dfs(x):
    for i in lst[x]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)


n,m = map(int,input().split())
visited = [0]*(n+1)
lst = [[] for _ in range(n+1)]
for i in range(m):
    s,e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
cnt= 0
for i in range(1,n+1):
    if visited[i]==0:
        visited[i]=1
        dfs(i)
        cnt+=1
print(cnt)
