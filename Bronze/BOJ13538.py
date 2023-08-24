N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
cnt = N
for i in A:
    i = i-B
    if i>0:
        if i%C:
            cnt+=i//C +1
        else:
            cnt+=i//C
print(cnt)