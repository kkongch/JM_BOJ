import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    a = int(input())
    if a==0 and not heap:
        print(0)
    elif a==0:
        print(heapq.heappop(heap))
    elif a!=0:
        heapq.heappush(heap,a)
