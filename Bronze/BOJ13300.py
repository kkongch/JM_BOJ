N,K = map(int,input().split())
lst_1 = []
lst_2 = []
for i in range(N):
    lst = list(map(int,input().split()))
    if lst[0]==0:
        lst_2.append(lst[1])
    elif lst[0]==1:
        lst_1.append(lst[1])
lst_1.sort()
lst_2.sort()
result=0
for i in range(6):
    if lst_1.count(i+1)%K==0:
        result+= lst_1.count(i+1)//K
    elif lst_1.count(i+1)%K!=0:
        result += lst_1.count(i + 1) // K + 1
    if lst_2.count(i + 1) % K == 0:
        result += lst_2.count(i + 1) // K
    elif lst_2.count(i+1)%K!=0:
        result += lst_2.count(i + 1) // K + 1

print(result)