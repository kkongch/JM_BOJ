import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = list(map(int,input().split()))
start, end = 0,n-1
ans = []
cnt = (start + end)//2
target = sum(lst)//m
while start<end:

    mid = (start + end)//2
    Sum = 0
    for i in range(start,mid):
        Sum+=lst[i]

