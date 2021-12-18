n = int(input())

a = 0
b = 1
c = a+b
for _ in range(n-1):
    c = a + b
    a = b
    b = c
if n == 0:
    print(0)
else:
    print(c)