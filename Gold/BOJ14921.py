n = int(input())
lst = list(map(int,input().split()))
lst.sort(lambda x:abs(x))
high, low = 0,0
Min = 21e8
result = []
while 1:
    if high-low+1<2:
        high+=1
        continue
    if abs(lst[high]+lst[low])<abs(Min):
        Min =lst[high]+lst[low]
        result.append(Min)
    low+=1
    if high==n-1 and high-low+1<2:
        break
result.sort(lambda x:abs(x))
print(result[0])
