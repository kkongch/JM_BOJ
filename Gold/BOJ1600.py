from collections import deque
#3차원 배열 bfs 
def bfs():
    while q:
        y,x,index,cnt = q.popleft()
        if y==h-1 and x==w-1:
            return cnt
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy>h-1 or dy<0 or dx>w-1 or dx<0:
                continue
            if lst[dy][dx]==1:
                continue
            if used[dy][dx]==-1:
                used[dy][dx]=cnt+1
                q.append([dy,dx,index,cnt+1])
            else:
                if used[dy][dx]>used[y][x]+1:
                    used[dy][dx]=used[y][x]+1
                    continue
                else:continue
        if index<k:
            for i in range(8):
                hy = y + horse_y[i]
                hx = x + horse_x[i]
                if hy>h-1 or hy<0 or hx>w-1 or hx<0:
                    continue
                if lst[hy][hx]==1:
                    continue
                if used[hy][hx]==-1:
                    used[hy][hx] = cnt+1
                    if horse_x[i]==-2:
                        if lst[y][x-1]==1:
                            q.append([hy, hx, index + 1, cnt + 1])
                    elif horse_x[i]==2:
                        if lst[y][x+1]==1:
                            q.append([hy, hx, index + 1, cnt + 1])
                    elif horse_y[i]==-2 :
                        if lst[y-1][x]==1:
                            q.append([hy, hx, index + 1, cnt + 1])
                    elif horse_y[i]==2:
                        if lst[y+1][x]==1:
                            q.append([hy, hx, index + 1, cnt + 1])
                else:
                    if used[hy][hx] > used[y][x]+1:
                        used[hy][hx] = used[y][x]+1
                        continue
                    else: continue
    return -1
# 말처럼 움직일 수 있는 가지수
k = int(input())
w,h = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(h)]

q = deque()
used = [[-1]*w for _ in range(h)]
horse_y = [-2,-2,-1,-1,2,2,1,1]
horse_x = [-1,1,-2,2,-1,1,-2,2]
dry = [-1,1,0,0]
drx = [0,0,-1,1]
# y좌표 x좌표 말의 이동 사용 횟수
q.append([0,0,0,0])
ret = bfs()
print(ret)