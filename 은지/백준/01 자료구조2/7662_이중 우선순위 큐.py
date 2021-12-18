import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in  range(T):
    k = int(input())
    min_queue = []
    max_queue = []
    chk = [x for x in range(k)]

    def clean(queue):
        while queue and chk[queue[0][1]]:
            heapq.heappop(queue)

    for i in range(k):
        s, v = input().split()
        if s == "I":
            heapq.heappush(min_queue, (int(v), i))
            heapq.heappush(max_queue, (-int(v), i))
            chk[i] = 0

        elif v == "-1":
            clean(min_queue)

            if min_queue:
                chk[min_queue[0][1]] = 1
                heapq.heappop(min_queue)
        else:
            clean(max_queue)

            if max_queue:
                chk[max_queue[0][1]] = 1
                heapq.heappop(max_queue)

    clean(min_queue)
    clean(max_queue)

    if min_queue and max_queue:
        print(-max_queue[0][0], min_queue[0][0])
    else:
        print("EMPTY")