com = int(input())
line = int(input())
lst = [list(map(int,input().split())) for _ in range(line)]
lst.sort(key=lambda x:int(x[2]))
arr=[0]*(com+1)

def findboss(member):
    global arr
    if arr[member]==0:
        return member
    ret = findboss(arr[member])
    arr[member] = ret
    return ret
def union(a,b,i):
    global arr,cnt,cost
    fa, fb = findboss(a),findboss(b)
    if fa == fb:
        return
    arr[fb] = fa
    cnt+=1
    cost+=(lst[i][2])

cnt,cost=0,0
for i in range(line):
    union(lst[i][0],lst[i][1],i)
print(cost)