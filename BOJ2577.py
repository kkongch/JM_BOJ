a = int(input())
b = int(input())
c = int(input())
result = a*b*c
st_result = list(str(result))

for i in range(10):
    print(st_result.count(str(i)))
