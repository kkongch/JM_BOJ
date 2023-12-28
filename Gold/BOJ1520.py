# bfs
# 이동할 수 있는 경로 모두 찾기
from collections import deque
def dfs(y,x):

    if y==m-1 and x==n-1:
        return 1
    if visit[y][x]:
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy>m-1 or dy<0 or dx>n-1 or dx<0:
                continue
            if path[y][x]>path[dy][dx]:
                visit[y][x]+=
    return h

# 지도의 세로의 크기 m 가로의 크기 n
m,n = map(int,input().split())
path = [list(map(int,input().split())) for _ in range(m)]
q = deque()
visit = [[-1]*n for _ in range(m)]
dry = [-1,1,0,0]
drx = [0,0,-1,1]
q.append([0,0])
ret =bfs()

print(ret)