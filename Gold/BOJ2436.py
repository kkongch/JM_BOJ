import math
def gcd(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a

n,m = map(int,input().split())

mul = n*m
for i in range(int(math.sqrt(mul)),0,-1):
    if mul%i ==0 and gcd(i,mul//i)==n:
        result = i
        break
print(result,mul//result)