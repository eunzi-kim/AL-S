import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

result = 0
tired = 0

for _ in range(24):
    if tired + A <= M:
        result += B
        tired += A
    else:
        tired -= C
        if tired < 0:
            tired = 0

print(result)