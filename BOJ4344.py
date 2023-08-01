testcase_num = int(input())
for i in range(testcase_num):
    lst = list(map(int,input().split()))
    cnt = 0
    SUM=0
    for k in range(lst[0]):
        SUM +=lst[k+1]
    avg = SUM/lst[0]
    for j in range(len(lst)-1):
        if lst[j+1]>avg:
            cnt+=1
    ratio = (cnt/lst[0]*100)
    print('{:.3f}%'.format(ratio))