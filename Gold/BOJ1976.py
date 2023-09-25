import sys

def findboss(member):
    global arr
    if arr[member]==0:
        return member
    ret = findboss(arr[member])
    arr[member]=ret
    return ret

def union(a,b):
    global arr
    fa,fb = findboss(a),findboss(b)
    if fa==fb:
        return 1
    arr[fb] = fa
    return 0
n = int(input())
m = int(input())
arr = [0]*(n+1)
lst = []
edge = []
for i in range(n):
    cycle = list(map(int,input().split()))
    lst.append(cycle)
for i in range(n):
    for k in range(len(cycle)):
        if lst[i][k] ==1:
            union(i+1,k+1)
plan = list(map(int,input().split()))
flag=0
for i in range(len(plan)-1):
    if findboss(plan[i])!=findboss(plan[i+1]):
        flag=1
        break

if flag:
    print('NO')
elif flag==0:
    print('YES')

