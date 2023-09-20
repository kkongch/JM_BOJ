import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    lst = map(int,input().split())
    for k in lst:
        if len(heap)<n:
            heapq.heappush(heap,k)
        else:
            if heap[0]<k:
                heapq.heappop(heap)
                heapq.heappush(heap,k)
print(heap[0])