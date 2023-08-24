N = int(input())
for _ in range(N):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.pop(0)
    b.pop(0)
    a.sort(reverse=True)
    b.sort(reverse=True)
    if a==b:
        print('D')
        continue
    if a.count(4)>b.count(4):
        print('A')
    elif a.count(4)==b.count(4) and a.count(3)>b.count(3):
        print('A')
    elif a.count(4)==b.count(4) and a.count(3)==b.count(3) and a.count(2)>b.count(2):
        print('A')
    elif a.count(4) == b.count(4) and a.count(3) == b.count(3) and a.count(2)== b.count(2) and a.count(1)>b.count(1):
        print('A')
    else:
        print('B')