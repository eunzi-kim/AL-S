import sys
input = sys.stdin.readline

import heapq

N = int(input())

arr = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, [abs(x), x])
    
    elif x == 0:
        if len(arr):
            x = heapq.heappop(arr)
            print(x[1])
        else:
            print(0)
