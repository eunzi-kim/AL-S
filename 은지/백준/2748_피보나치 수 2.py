import sys
input = sys.stdin.readline

n = int(input())

# def fibo(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fibo(x-1) + fibo(x-2)
# print(fibo(n))

ans = 1
a = 0
b = 1
for _ in range(n-1):
    c = a+b
    a = b
    b = c
    ans = c

print(ans)