t = int(input())
for tc in range(t):
    p = input()
    n = int(input())
    In = list(map(int,input()[1:-1].replace(',','')))
    print(In)
    # lst =[]
    # flag =0
    # for i in range(len(In)):
    #     if In[i].isdigit() == True:
    #         lst.append(int(In[i]))
    # for i in range(len(p)):
    #     if p[i]=='R':
    #         lst.reverse()
    #     elif p[i]=='D':
    #         if not lst:
    #             flag=1
    #             break
    #         lst.pop(0)
    # if flag == 1:
    #     print('error')
    # else:
    #     print(lst)
