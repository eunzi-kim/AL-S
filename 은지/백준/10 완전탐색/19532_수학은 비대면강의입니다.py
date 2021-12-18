a, b, c, d, e, f = map(int, input().split())

if (b*d)-(a*e) == 0:
    y = 0
else:
    y = ((c*d)-(a*f)) / ((b*d)-(a*e))

if a == 0:
    x = (f-(e*y)) / d
else:
    x = (c-(b*y)) / a

print(int(x), int(y))


############################################

a, b, c, d, e, f = map(int, input().split())

def math(a, b, c, d, e, f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x+b*y == c and d*x+e*y == f:
                return [x, y]

ans = math(a, b, c, d, e, f)
print(*ans)