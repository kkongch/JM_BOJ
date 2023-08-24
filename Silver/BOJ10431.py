import copy
tc = int(input())
for test_case in range(1,tc+1):
    lst = list(map(int,input().split()))
    cnt = 0
    for i in range(1,len(lst)-1):
        for k in range(1,len(lst)-i):
            if lst[k]>lst[k+1]:
                temp = copy.deepcopy(lst[k+1])
                lst[k+1] = lst[k]
                lst[k] = temp
                cnt+=1
    print(f'{lst[0]} {cnt}')
