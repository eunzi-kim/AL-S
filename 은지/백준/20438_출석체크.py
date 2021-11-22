import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleep = list(map(int, input().split()))
code = list(map(int, input().split()))

chk = [1] * (N+3)  # 3 ~ N+2
# chk[0] = chk[1] = chk[2] = 0
for x in code:
    if x not in sleep:
        for v in range(x, N+3, x):
            if v not in sleep:
                chk[v] = 0

sum_chk = [0] * (N+3)
for i in range(3, N+3):
    sum_chk[i] = sum_chk[i-1] + chk[i]

for _ in range(M):
    S, E = map(int, input().split())
    print(sum_chk[E]-sum_chk[S-1])