lst = [list(map(int,input().split())) for _ in range(4)]

arr = [[0]*100 for _ in range(100)]
for i in range(4):
    for j in range(lst[i][0],lst[i][2]):
        for k in range(lst[i][1],lst[i][3]):
            arr[j][k] = 1

result = 0
for i in arr:
    cnt = i.count(1)
    result+=cnt
print(result)
