n,m = map(int,input().split())
dic = {}
for i in range(n):
    site,pw = input().split()
    dic[site] = pw
for i in range(m):
    st = input()
    print(dic.get(st))
