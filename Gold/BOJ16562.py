import sys
sys.setrecursionlimit(100000)

def findboss(member):
    global arr
    if arr[member]==0:
        return member
    ret = findboss(arr[member])
    arr[member] = ret
    return ret


def union(a,b):
    global arr
    fa,fb = findboss(a),findboss(b)
    if fa==fb:
        return
    if money_lst[fa]>=money_lst[fb]:
        arr[fa]=fb
    else:
        arr[fb]=fa


n,m,j = map(int,input().split())
arr =[-1]+[0]*(n)
lst = []
money_lst =[0]+list(map(int,input().split()))

for i in range(m):
    v,w = map(int,input().split())
    lst.append([v,w])

for i in range(len(lst)):
    union(lst[i][0],lst[i][1])

Min = 0
for i in range(1,len(arr)):
    if arr[i]==0:
        Min+=money_lst[i]

if Min>j:
    print('Oh no')
else:
    print(Min)



