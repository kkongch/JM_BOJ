from collections import deque
def bfs():
    cnt = 0
    while q:
        y,x = q.popleft()
        for i in range(5):
            dy = y+directy[i]
            dx = x+directx[i]
            if dy<0 or dx<0 or dy>m-1 or dx>n-1:
                continue
            if lst[dy][dx] ==1:
                continue
            q.append([dy,dx])
            lst[dy][dx]=1
            cnt += 1
    return cnt

m,n,k = map(int,input().split())
lst = [[0]*n for i in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for k in range(y1,y2):
        for j in range(x1,x2):
            lst[k][j]=1
q = deque()
result = []
directy = [0,1,-1,0,0]
directx = [0,0,0,-1,1]
Count =0
for i in range(m):
    for k in range(n):
        if lst[i][k]==0:
            q.append([i,k])
            ret = bfs()
            Count+=1
            result.append(ret)
result.sort()
print(Count)
print(*result)