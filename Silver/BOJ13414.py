import sys
input = sys.stdin.readline
k,l = map(int,input().split())
dic = {}
for i in range(l):
    st = input().strip()
    dic[st] = i

lst = list(dic.items())
lst.sort(key=lambda x:x[1])

if len(lst)<k:
    a = len(lst)
else:
    a = k
for i in range(a):
    print(lst[i][0])