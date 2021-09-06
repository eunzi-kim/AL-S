from itertools import permutations

N, M = map(int, input().split())

for i in permutations(range(1, N+1), M):
    print(" ".join(map(str, i)))
    # print(*i)