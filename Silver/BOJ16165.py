n,m = map(int,input().split())
dic =dict()
for i in range(n):
    group = input()
    dic[group] = ['']
    for k in range(int(input())):
        dic[group].append(input())

for i in range(m):
    st = input()
    num = int(input())
    if num:
        lst_1 = list(dic.keys())
        lst_2 = list(dic.values())
        for i in range(n):
            if st in lst_2[i]:
                Index = i
        print(lst_1[Index])

    else:
        lst = dic.get(st)
        lst.pop(0)
        lst.sort()
        for i in lst:
            print(i)