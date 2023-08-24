num = int(input())
lst = [list(map(int,input().split())) for _ in range(num)]
result=[]
friend ={1:6,2:4,3:5,6:1,4:2,5:3}

for j in range(6):
    side=[]
    top = lst[0][j]
    for i in range(num):
        bottom=top
        if lst[i].index(bottom)==0:
            top = lst[i][friend.get(1)-1]
            Max = 0
            for k in range(6):
                if k!=lst[i].index(top) and k!=lst[i].index(bottom):    #bcde
                    if lst[i][k]>Max:
                        Max = lst[i][k]
            side.append(Max)
        elif lst[i].index(bottom)==1: #b
            top = lst[i][friend.get(2)-1]
            Max = 0
            for k in range(6):
                if k!=lst[i].index(top) and k!=lst[i].index(bottom):    #bcde
                    if lst[i][k] > Max:
                        Max = lst[i][k]
            side.append(Max)
        elif lst[i].index(bottom)==2: #c
            top = lst[i][friend.get(3)-1]
            Max = 0
            for k in range(6):
                if k!=lst[i].index(top) and k!=lst[i].index(bottom):    #bcde
                    if lst[i][k] > Max:
                        Max = lst[i][k]
            side.append(Max)
        elif lst[i].index(bottom)==3: #d
            top = lst[i][friend.get(4)-1]
            Max = 0
            for k in range(6):
                if k!=lst[i].index(top) and k!=lst[i].index(bottom):    #bcde
                    if lst[i][k] > Max:
                        Max = lst[i][k]
            side.append(Max)
        elif lst[i].index(bottom)==4: #e)
            top = lst[i][friend.get(5)-1]
            Max = 0
            for k in range(6):
                if k!=lst[i].index(top) and k!=lst[i].index(bottom):    #bcde
                    if lst[i][k] > Max:
                        Max = lst[i][k]
            side.append(Max)
        elif lst[i].index(bottom)==5:
            top = lst[i][friend.get(6)-1] #a
            Max = 0
            for k in range(6):
                if k!=lst[i].index(top) and k!=lst[i].index(bottom):    #bcde
                    if lst[i][k] > Max:
                        Max = lst[i][k]
            side.append(Max)

    result.append(sum(side))

print(max(result))