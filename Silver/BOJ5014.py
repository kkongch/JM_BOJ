from collections import deque
def bfs():
    visit = [0] * (f + 1)
    while q:
        stairs,cnt = q.popleft()
        if stairs==g:
            return cnt
        if stairs+u<=f and visit[stairs+u]==0:
            visit[stairs+u]=1
            cnt+=1
            q.append([stairs+u,cnt])
        if stairs-d>=0 and visit[stairs-d]==0 :
            cnt+=1
            visit[stairs-d]=1
            q.append([stairs-d,cnt])

    return -1


import sys
input = sys.stdin.readline
f,s,g,u,d = map(int,input().split())
q = deque()
q.append([s,0])
ret = bfs()

if ret == -1:
    print('use the stairs')
else:
    print(ret)