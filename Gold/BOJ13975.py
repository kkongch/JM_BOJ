import sys
import heapq
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    cost=[]
    heap = list(map(int,input().split()))
    heapq.heapify(heap)

    result = []
    while 1:
        if len(heap)==1:
            break
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap,(a+b))
        cost.append(a+b)
    print(sum(cost))
