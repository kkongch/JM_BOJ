import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    a = int(input())
    if a==0 and not heap:
        print(0)
    elif a!=0:
        heapq.heappush(heap,-a)
    elif a==0:
        x = heapq.heappop(heap)
        print(-x)
