import sys
input = sys.stdin.readline

N = int(input())

x = 0
y = 1
for i in range(1, N):
    temp = x + y
    x = y
    y = temp

if N == 0:
    print(0)
else:
    print(y)