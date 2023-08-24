rollcake = int(input())
N = int(input())
lst = [0]*(rollcake+1)
Max =0
for i in range(1,N+1):
    P,K = map(int,input().split())
    if K-P+1>Max:
        Max = K-P+1
        Index = i
    for k in range(P,K+1):
        if lst[k]==0:
            lst[k] = i
Max_2 = 0

for i in range(1,N+1):
    if lst.count(i)>Max_2:
        Max_2 = lst.count(i)
        Index_2 = i

print(Index)
print(Index_2)

