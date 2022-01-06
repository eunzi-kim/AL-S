N = int(input())
arr= list(map(int, input().split()))
M = int(input())

s = 1
e = max(arr)

while s <= e:
    m = (s+e)//2

    temp = 0
    for x in arr:
        temp += min(m, x)
    
    if temp <= M:
        s = m+1
    else:
        e = m-1

print(e)