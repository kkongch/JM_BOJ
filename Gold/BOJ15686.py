import sys,copy
def combi(level,start):
    if level == m:
        combi_arr.append(path[:])
        return
    for i in range(start, len(chickenlist)):
        path[level] = i
        combi(level+1, i+1)

input = sys.stdin.readline
n,m = map(int,input().split())
citymap = [list(map(int,input().split())) for _ in range(n)]
houselist = [] # 집 위치 리스트
chickenlist = [] # 치킨집 위치 리스트
combi_arr = [] #치킨집 위치 조합
arr = []
for i in range(n):
    for k in range(len(citymap[i])):
        if citymap[i][k] == 1:
            houselist.append([i,k])
        elif citymap[i][k]==2:
            chickenlist.append([i,k])

path = ['']*m
Min = 0
result = 21e8
combi(0,0)
c_length = [21e8]*m
for i in range(len(combi_arr)):
    for k in range(len(houselist)):
        for j in range(m):
            c_length[j] = abs(houselist[k][0]-chickenlist[combi_arr[i][j]][0])+abs(houselist[k][1]-chickenlist[combi_arr[i][j]][1])
            # if c_length[j]==1:
            #     break
        Min += min(c_length)
    if result>Min:
        result = Min
    Min = 0
print(result)
