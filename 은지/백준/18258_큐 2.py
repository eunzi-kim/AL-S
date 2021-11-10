import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
cnt = 0

for _ in range(N):
    arr = list(input().split())

    if arr[0] == "push":
        queue.append(arr[1])
        cnt += 1
    elif arr[0] == "pop":
        if cnt:
            v = queue.popleft()
            print(v)
            cnt -= 1
        else:
            print(-1)
    elif arr[0] == "size":
        print(cnt)
    elif arr[0] == "empty":
        if cnt:
            print(0)
        else:
            print(1)
    elif arr[0] == "front":
        if cnt:
            print(queue[0])
        else:
            print(-1)
    else:
        if cnt:
            print(queue[cnt-1])
        else:
            print(-1)