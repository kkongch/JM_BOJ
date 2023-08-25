N,K  = map(int,input().split())
lst= list(map(int,input().split()))
Sum = 0

for i in range(K):
    Sum += lst[i]
Max = Sum
for i in range(N-K):
    Sum += lst[i+K]
    Sum -= lst[i]
    if Max < Sum:
        Max = Sum


print(Max)