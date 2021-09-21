import sys

input = sys.stdin.readline

# print(input())
n = int(input())

answer = 0
a = 0
s = 0
while s <=n:
    a += 1
    s = 5 * a


# print(n, s, a)
a = a-1
d = 0
e = 0
# print(a)

for aa in range(a, -1, -1):
    # print(aa)
    c = n - (5*aa)

    e = aa
    if c % 2 == 0:
        d = c // 2
        

        break

answer = e + d
if n != (e*5) + (d*2):
    answer = -1
print(answer)





