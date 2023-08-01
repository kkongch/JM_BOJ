num = int(input())
for i in range(num):
    test_num,st = map(str,input().split())
    for k in st:
        print(k*int(test_num),end='')
    print()