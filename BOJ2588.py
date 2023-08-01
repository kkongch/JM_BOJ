num_1 = int(input())
num_2 = int(input())
num_3 = list(map(int,str(num_2)))

result = [0,0,0]
mul = num_1 * num_2
for i in range(3):
    result[i] = num_1 * num_3[2-i]
result.append(mul)
for i in range(4):
    print(result[i])