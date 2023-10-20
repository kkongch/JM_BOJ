# bfs
# 먼저 걸리는 시간 계산 --> bfs
# 걸리는 시간 -1시간 계산 --> check
import copy
from collections import deque


def bfs():
    q.append([0,0])
    while q:
        y, x= q.popleft()

        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy < 0 or dy > col - 1 or dx < 0 or dx > row - 1:
                continue
            if visit[dy][dx] == 0:
                visit[dy][dx]=1
                if lst[dy][dx]==0:
                    q.append([dy,dx])
                elif lst[dy][dx]==1:
                    melt.append([dy,dx])
    for y,x in melt:
        lst[y][x]=0
    return len(melt)




def check():
    pass


col, row = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(col)]
dry = [1, -1, 0, 0]
drx = [0, 0, -1, 1]
q = deque()
num = 0
for i in range(col):
    for k in range(row):
        if lst[i][k]==1:
            num+=1
cnt=1
while 1:
    melt = []

    visit = [[0] * row for _ in range(col)]
    ret = bfs()
    num-=ret

    if num==0:
        print(cnt)
        print(ret)
        break
    cnt+=1

# for i in lst:
#     print(*i)
#
