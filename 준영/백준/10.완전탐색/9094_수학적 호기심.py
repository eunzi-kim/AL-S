import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = 0

    for i in range(1, N):
        for j in range(1, i):
            x = ((i**2) + (j**2) + M) / (i*j)
            if x - int(x) == 0:
                result += 1

    print(result)