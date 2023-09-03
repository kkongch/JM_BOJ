from collections import deque
def bfs():
    global Map

    # visited = [[0]*m for _ in range(n)]
    while q:
        yy,xx = q.popleft()

        for i in range(4):
            dy = directy[i]+yy
            dx = directx[i]+xx
            if dy>n-1 or dx>m-1 or dx<0 or dy<0 or Map[dy][dx]==0:
                continue
            # visited[dy][dx]=1
            Map[dy][dx] =0
            q.append([dy,dx])


tc  = int(input())
for t in range(tc):
    cnt=0
    directy = [1,-1,0,0]
    directx = [0,0,-1,1]
    m,n,k = map(int,input().split())
    Map = [[0]*m for _ in range(n)]
    q = deque()

    for i in range(k):
        x,y = map(int,input().split())
        Map[y][x]=1
    for i in range(n):
        for k in range(m):
            if Map[i][k] == 1:
                q.append([i,k])
                Map[i][k] = 0
                bfs()
                cnt += 1
    print(cnt)
