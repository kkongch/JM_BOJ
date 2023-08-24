import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        stack.append(s[1])
    elif s[0] == 'pop':
        if stack:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif s[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)