import sys
input = sys.stdin.readline

N = int(input())

min_val = -1

x = N % 5 - 1
y = N // 5 if N % 5 else N // 5 - 1

arr = [2, 1, 3, 2, 1]
arr2 = [-1, 1, -1, 2, 1]

if y == 0:
    result = arr2[x]
else:
    result = y + arr[x]

print(result)