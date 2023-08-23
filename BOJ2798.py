N,M = map(int,input().split())
lst = list(map(int,input().split()))
path = []
result = []
used = [0]*(N+1)
Max = 0
def abc(level,start):
    global Max
    if level==3:
        if sum(path)<=M and Max < sum(path):
            Max = sum(path)
        return

    for i in range(start,len(lst)):
        if used[i]==0:
            used[i]= 1
            path.append(lst[i])
            abc(level+1,start+1)
            path.pop()
            used[i]=0
abc(0,0)


print(Max)