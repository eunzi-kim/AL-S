import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = max(arr)

while s <= e:
    m = (s+e)//2

    branch = 0 
    for tree in arr:
        if tree > m:
            branch += tree-m

    if branch == M:
        break
    elif branch < M:
        e = m-1        
    else:
        s = m+1

print((s+e)//2)