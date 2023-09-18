n = int(input())
lst = list(map(int, input().split()))
lst.sort(lambda x:abs(x))
high,low = 0,0
Min = 21e8
while 1:
    if high-low+1 <2:
        high+=1
        continue
    if abs(lst[high]+lst[low])<Min:
        result = []
        Min = abs(lst[high]+lst[low])
        result.append(lst[high])
        result.append(lst[low])
    low+=1
    if high == n-1 and high-low+1<2:
        break
result.sort()
print(*result)