st = input().split('-')
Min_Sum,Max_Sum = 0,0
lst = []

for i in st[0].split('+'):
    Max_Sum+=int(i)
for i in st[1:]:
    for j in i.split('+'):
        Min_Sum-=int(j)


print(Max_Sum+Min_Sum)

