# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# arr = [[] for _ in range(N+1)]

# for i in range(M):
#     a, b = map(int, input().split())
#     arr[b].append(a)

# count = [0 for _ in range(N+1)]

# for i in range(N, -1, -1):
#     temp = 0
#     q = arr[i][:]

#     while q:
#         x = q.pop(0)
#         if count[x]:
#             temp += count[x]
#         else:
#             temp += 1

#             for j in arr[x]:
#                 q.append(j)

#     count[i] = temp

# result = []

# for i in range(1, N+1):
#     if max(count) == count[i]:
#         result.append(i)

# print(*result)


import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for _ in range(n + 1)]
    visit[start] = 1
    cnt = 1
    while q:
        st = q.popleft()
        for i in s[st]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt

n, m = map(int, input().split())

s = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    s[b].append(a)
    
result = []

max_cnt = 0

for i in range(1, n + 1):
    tmp = bfs(i)
    if max_cnt == tmp:
        result.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        result = []
        result.append(i)
        
print(*result)