n = int(input())
lst = []
result = []
stack = []
c = 1
flag =0
for i in range(n):
    num = int(input())
    while c <= num:
        stack.append(c)
        result.append('+')
        c+=1
    if stack[-1]==num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        flag=1
        break
if not flag:
    for i in range(len(result)):
        print(result[i])

