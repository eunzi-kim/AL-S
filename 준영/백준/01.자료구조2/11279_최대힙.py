import heapq
import sys

input = sys.stdin.readline

N = int(input())

arr = []
result = []
for i in range(N):
    temp = int(input())
    
    if temp != 0:
        heapq.heappush(arr, -temp)
    else:
        if len(arr) == 0:
            result.append(0)
        else:
            a = heapq.heappop(arr)
            result.append(-a)

for i in result:
    print(i)
