import math
m,n = map(int,input().split())
end = int(math.sqrt(n))
check = [0]*(n+1)
for i in range(2,end+1):
    if check[i]==1: continue
    for j in range(i+i,n+1,i):
        check[j]=1
for i in range(m,n+1):
    if check[i]==0 and i!=1:
        print(i)