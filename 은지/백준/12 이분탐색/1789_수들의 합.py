S = int(input())

sum_n = 0
x = 1
while sum_n+x <= S:
    sum_n += x
    x += 1
print(x-1)