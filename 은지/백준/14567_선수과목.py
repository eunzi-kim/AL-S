import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rank = [1] * (N+1)  # 차수 degree
child = [[x] for x in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    if rank[B] < rank[A]+1:
        d = rank[A] + 1 - rank[B]
        for x in child[B]:
            if x not in child[A]:
                child[A].append(x)
            rank[x] = max(rank[x], rank[x]+d)

print(' '.join(map(str, rank[1:])))