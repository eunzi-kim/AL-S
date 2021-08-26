n, k = map(int, input().split())

answer = "<"
p = [x for x in range(1, n+1)]
i = k-1
while len(p) > 1:        
    v = p.pop(i)
    i = (k+i-1) % len(p)
    answer += str(v) + ", "
v = p.pop(0)
answer += str(v) + ">"

print(answer)