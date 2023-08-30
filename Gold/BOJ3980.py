def dfs(level):
    global Max
    if level==11:
        if Max < sum(stats):
            Max = sum(stats)
        return

    for i in range(11):
        if visited[i]==0 and lst[level][i]!=0:
            stats.append(lst[level][i])
            visited[i]=1
            dfs(level+1)
            stats.pop()
            visited[i]=0

tc = int(input())
for _ in range(tc):
    lst = [list(map(int,input().split())) for _ in range(11)]
    visited = [0]*11
    stats = []
    Max = 0
    dfs(0)
    print(Max)