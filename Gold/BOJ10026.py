from collections import deque
import copy
def bfs(target,number):
    global cnt_1
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y+dry[i]
            dx = x+drx[i]
            if dy<0 or dy>=n or dx<0 or dx>=n or used[dy][dx]==1:
                continue
            if lst[dy][dx] != target:
                continue
            lst[dy][dx] = number
            used[dy][dx]=1
            q.append([dy,dx])
    cnt_1+=1
def new_bfs(target,number):
    global cnt_2
    while q_1:
        y,x = q_1.popleft()
        for i in range(4):
            dy = y+dry[i]
            dx = x+drx[i]
            if dy<0 or dy>=n or dx<0 or dx>=n or used_1[dy][dx]==1:
                continue
            if lst_1[dy][dx] != target:
                continue
            lst_1[dy][dx] = number
            used_1[dy][dx]=1
            q_1.append([dy,dx])
    cnt_2+=1

n = int(input())
lst = [list(input()) for _ in range(n)]
lst_1 = copy.deepcopy(lst)
cnt_1,cnt_2 = 0,0
drx = [0,0,-1,1]
dry = [1,-1,0,0]
used = [[0]*len(lst) for _ in range(n)]
used_1 = [[0]*len(lst) for _ in range(n)]
q = deque()
num_1 = 1
num_2 = 1
for i in range(n):
    for k in range(n):
        if lst[i][k]== 'B' or lst[i][k]== 'G' or lst[i][k]== 'R':
            q.append([i,k])
            bfs(lst[i][k],num_1)
            num_1+=1
q_1 = deque()
for i in range(n):
    for k in range(n):
        if lst_1[i][k] == 'G':
            lst_1[i][k] ='R'
for i in range(n):
    for k in range(n):
        if lst_1[i][k] == 'B' or lst_1[i][k] == 'G' or lst_1[i][k] == 'R':
            q_1.append([i,k])
            new_bfs(lst_1[i][k],num_2)
            num_2+=1
print(cnt_1)
print(cnt_2)