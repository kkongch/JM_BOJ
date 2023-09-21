lst = []
n = int(input())
for i in range(n):
    name,ps = input().split()
    if ps == 'enter':
        lst.append(name)
    elif ps =='leave':
        lst.remove(name)
lst.sort(reverse=True)
for i in lst:
    print(i)