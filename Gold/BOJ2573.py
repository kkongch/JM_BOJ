from collections import deque
import copy
def bfs():
    while q:
        cnt = 0
        y,x = q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1:
                continue
            if bingsan[dy][dx]==0:
                cnt+=1
        cnt_lst[y][x]=cnt
def check():
    while v_q:
        y, x = v_q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1 or used[dy][dx]==1 or visit[dy][dx]==0:
                continue
            used[dy][dx]=1
            visit[dy][dx] = 0
            v_q.append([dy,dx])

n,m = map(int,input().split())
bingsan = [list(map(int,input().split())) for _ in range(n)]
q = deque()
v_q = deque()
dry = [1,-1,0,0]
drx = [0,0,-1,1]
year = 0
while 1:
    cnt = 0
    cnt_lst = [[0] * m for _ in range(n)]
    used = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if bingsan[i][k]!=0:
                q.append([i,k])
    bfs()
    year+=1
    for i in range(n):
        for k in range(m):
            bingsan[i][k] -= cnt_lst[i][k]
            if bingsan[i][k]<0:
                bingsan[i][k]=0
    visit = copy.deepcopy(bingsan)

    for i in range(n):
        for k in range(m):
            if visit[i][k]!=0:
                v_q.append([i,k])
                check()
                cnt+=1

    if cnt>=2:
        break
    elif cnt==0:
        print(0)
        exit(0)
print(year)