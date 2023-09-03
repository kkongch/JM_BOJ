from collections import deque
def bfs():
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]
            if dy<0 or dx<0 or dy>m-1 or dx>n-1:
                continue
            if tomato[dy][dx] ==0:
                tomato[dy][dx] = tomato[y][x]+1
                q.append([dy,dx])


n,m = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(m)]

q = deque()
directx = [0,0,-1,1]
directy = [1,-1,0,0]
for i in range(m):
    for k in range(n):
        if tomato[i][k] == 1:
            q.append([i,k])
if not q:
    print(-1)
    exit(0)
bfs()
Max = 0
for i in range(m):
    for k in range(n):
        if Max<tomato[i][k]:
            Max = tomato[i][k]
        if tomato[i][k]==0:
            print(-1)
            exit(0)

if Max == 1:
    print(0)
else:
    print(Max-1)


