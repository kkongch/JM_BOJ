N = int(input())
lst = list(map(int,input().split()))
line = []
for i in range(N):
    if i==0:
        line.append(i+1)
    else:
        line.insert(i-lst[i],i+1)
print(*line)