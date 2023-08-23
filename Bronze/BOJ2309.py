lst =[]
for i in range(9):
    a = int(input())
    lst.append(a)

path= []
visited = [0]*9
flag=0
def abc(level,start):
    global flag
    if level ==7 and flag==0:
        if sum(path)==100:
            flag=1
            path.sort()
            for i in range(7):
                print(path[i])
            return
        return

    for i in range(start,9):
        if visited[i]==0:
            visited[i]=1
            path.append(lst[i])
            abc(level+1,start+1)
            path.pop()
            visited[i]=0

abc(0,0)
