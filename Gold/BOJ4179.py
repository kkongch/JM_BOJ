from collections import deque
# import sys
# input = sys.stdin.readline
#
def f_bfs():
    while f_q:
        y,x,f_cnt = f_q.popleft()
        used_f[y][x]=1
        for i in range(4):
            dy = y+dry[i]
            dx = x+drx[i]
            if dy>r or dx>c or dy<1 or dx<1 or lst[dy][dx] =='#' or lst[dy][dx]=='F':
                continue
            if used_f[dy][dx] == 1:
                continue
            used_f[dy][dx]=1
            lst[dy][dx] = f_cnt
            f_q.append([dy,dx,f_cnt+1])
def bfs():
    global Min
    while q:
        # print(q)
        y, x, cnt = q.popleft()
        used[y][x] = 1
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy > r+2 or dx > c+2 or dy < 0 or dx < 0 or lst[dy][dx]=='#' or lst[dy][dx]=='F' :
                continue
            if used[dy][dx] == 1:
                continue
            if lst[dy][dx]!='.' and cnt+1>=lst[dy][dx]:
                if lst[dy][dx]==0:
                    if Min>cnt+1:
                        Min = cnt+1
                continue
            used[dy][dx]=1
            q.append([dy,dx,cnt+1])


Min = 21e8
lst = []
result = []
r,c = map(int,input().split())
used = [[0]*(c+2) for _ in range(r+2)]
used_f = [[0]*(c+2) for _ in range(r+2)]
lst.append([0]*(c+2))
for i in range(r):
    lst.append([0]+list(input().rstrip())+[0])
lst.append([0]*(c+2))

dry = [1,-1,0,0]
drx = [0,0,-1,1]
q = deque()
f_q = deque()
for i in range(r+2):
    for k in range(c+2):
        if lst[i][k]=='J':
            q.append([i,k,0])
        if lst[i][k]=='F':
            f_q.append([i,k,1])
if f_q:
    f_bfs()
# for i in lst:
#     print(*i)
bfs()
if Min!= 21e8:
    print(Min)
else:
    print('IMPOSSIBLE')

