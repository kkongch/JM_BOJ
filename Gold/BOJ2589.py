from collections import deque
col, row = map(int,input().split())
lst = [input() for _ in range(col)]
directy = [1,-1,0,0]
directx = [0,0,-1,1]

def bfs(y,x):
    visited = [[0]*row for _ in range(col)]
    q = deque()
    q.append([y,x,0])
    visited[y][x]=1
    while q:
        y,x,cnt = q.popleft()

        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]

            if dy<0 or dx<0 or dy>col-1 or dx>row-1:
                continue
            if visited[dy][dx] == 0:
                if lst[dy][dx] == 'L':
                    visited[dy][dx] = 1
                    q.append([dy,dx,cnt+1])

    return cnt
Max=0
for i in range(col):
    for k in range(row):
        if lst[i][k]=='L':
            ret = bfs(i,k)
            if Max <ret:
                Max=ret


print(Max)