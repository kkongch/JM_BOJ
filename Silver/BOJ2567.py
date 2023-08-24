paper = [[0]*100 for _ in range(100)]
N = int(input())
directy = [1,-1,0,0]
directx = [0,0,-1,1]
for i in range(N):
    x,y = map(int,input().split())
    for k in range(y,y+10):
        for j in range(x,x+10):
            paper[100-k][j]=1


# for i in paper:
#     print(*i)
result=0

for i in range(100):
    for k in range(100):
        if paper[i][k]==1:
            cnt=0
            for j in range(4):
                dy = directy[j] + i
                dx = directx[j] + k

                if dy<0 or dx<0 or dy>99 or dx>99:
                    continue
                if paper[dy][dx]==1:
                    cnt+=1
            if cnt==2:
                result+=1
            if cnt==2 or cnt==3:
                result+=1
print(result)