import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = 0
b = 0 

result = []

while a < len(A) and b < len(B):
    if A[a] < B[b]:
        result.append(A[a])
        a += 1
    else:
        result.append(B[b])
        b += 1

result += A[a:]
result += B[b:]

print(' '.join(map(str, result)))