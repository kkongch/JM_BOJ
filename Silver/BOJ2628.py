row,col  = map(int,input().split())
N = int(input())
width,height = [0,row],[0,col]
for i in range(N):
    a,b = map(int,input().split())
    if a==0:
        height.append(b)
    else:
        width.append(b)
width.sort()
height.sort()
result=[]
for i in range(len(width)-1):
    for k in range(len(height)-1):
        area = abs(width[i]-width[i+1]) * abs(height[k]-height[k+1])
        result.append(area)

print(max(result))