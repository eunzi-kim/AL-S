N, M = map(int, input().split())
S = [input() for _ in range(N)]

cnt = 0
for _ in range(M):
    if input() in S:
        cnt += 1

print(cnt)