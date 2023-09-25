from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    while q:
        start,result= q.popleft()
        if used[start]==0:
            used[start]=1
            if start == 100:
                return result
            for i in range(1,7):
                for k in range(n):
                    if start == sadari[k][0]:
                        start = sadari[k][1]

                for k in range(m):
                    if start ==bem[k][0]:
                        start = bem[k][1]
                if start>100:
                    continue
                q.append([start+i,result+1])

n,m = map(int,input().split())

sadari = [list(map(int,input().split())) for _ in range(n)]
bem = [list(map(int,input().split())) for _ in range(m)]
used = [0]*101
path = 1
q = deque()
q.append([path,0])
ret = bfs()
print(ret)
