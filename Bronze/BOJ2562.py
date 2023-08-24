lst = []
MAX = 0
for i in range(9):
    lst.append(int(input()))
for i in lst:
    if i>MAX:
        MAX=i
    
print(MAX)
print(lst.index(MAX)+1)
