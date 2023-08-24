num = int(input())
SUM = [0]*num


for i in range(num):
    a, b = map(int, input().split())
    SUM[i] = a+b

for i in SUM:
    print(i)