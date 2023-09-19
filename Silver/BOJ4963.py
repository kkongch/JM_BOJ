from collections import deque
def bfs():
    while q:
        y,x = q.popleft()
        for i in range(8):
            dy = y+directy[i]
            dx = x+directx[i]
            if dy<0 or dx<0 or dy>h-1 or dx>w-1 or Map[dy][dx] == 0:
                continue
            Map[dy][dx] = 0
            q.append([dy,dx])
directy = [1,-1,0,0,-1,1,-1,1]
directx = [0,0,-1,1,1,1,-1,-1]
while 1:
    q = deque()
    Map = []
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    for i in range(h):
        Map.append(list(map(int,input().split())))
    cnt = 0
    for i in range(h):
        for k in range(w):
            if Map[i][k]== 1:
                q.append([i,k])
                bfs()
                cnt+=1
    print(cnt)