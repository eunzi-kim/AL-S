import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())

    tree[B][A] = 1

level = 1

result = [0 for _ in range(N+1)]

while True:
    temp = [i[:] for i in tree]
    cnt = 0
    for i in range(1, N+1):
        if result[i]:
            cnt += 1
            continue
        if tree[i].count(0) == (N+1):
            result[i] = level
            for j in range(i+1, N+1):
                temp[j][i] = 0

    if cnt == N:
        break
    tree = [i[:] for i in temp]
    level += 1

print(' '.join(map(str, result[1:])))