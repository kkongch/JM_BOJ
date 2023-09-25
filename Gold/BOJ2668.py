def dfs(num):
    global result,lst,arr,number

    if used[num]==1:
        return
    if used[num]==0:
        result.append([num,lst[num]])
        used[num]=1
        dfs(lst[num])
    if result:
        if result[-1][1]!=number:
            result=[]


n = int(input())
lst= [0]
arr = []
for i in range(n):
    arr.append(i+1)
    lst.append(int(input()))
# print(lst)
result = []
result_1=[]
for i in arr:
    used = [0]*(len(arr)+1)
    number = i
    dfs(i)
    if result:
        for k in result:
            result_1.append(k[0])
result_1.sort()
print(len(set(result_1)))
for i in set(result_1):
    print(i)
