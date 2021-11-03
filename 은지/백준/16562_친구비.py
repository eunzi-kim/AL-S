import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# 저렴한 친구 기준
cheap_friend = [x for x in range(N+1)]

def find(x):
    if cheap_friend[x] == x:
        return cheap_friend[x]
    else:
        cheap_friend[x] = find(cheap_friend[x])
        return cheap_friend[x]

def union(a, b):
    friend_a = find(a)
    friend_b = find(b)
    if arr[friend_a] <= arr[friend_b]:
        cheap_friend[friend_b] = cheap_friend[friend_a]
    else:
        cheap_friend[friend_a] = cheap_friend[friend_b]

for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)
    

# 친구 비용 탐색
ans = 0
visited = [0] * (N+1)
for i in range(1, N+1):
    idx = find(cheap_friend[i])

    if visited[idx]:
        continue
    
    visited[idx] = 1
    ans += arr[idx]


# 출력
if ans > k:
    print("Oh no")
else:
    print(ans)