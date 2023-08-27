N = int(input())
lst=[0]*1001

Max_index,Max = 0,0
for _ in range(N):
    L,M = map(int,input().split())
    lst[L] = M
    if Max<M:
        Max_index,Max = L,M
ans, Max = 0,0
for i in range(Max_index+1):
    Max = max(Max,lst[i])
    ans +=Max
Max = 0
for i in range(1000,Max_index,-1):
    Max = max(Max,lst[i])
    ans+=Max
print(ans)