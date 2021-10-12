K = int(input())
arr = list(map(int, input().split()))

ans = [[] for _ in range(K)]


def tree(start, end, level):
    if start == end:
        ans[level].append(arr[start])
        return
    
    i = (start + end) // 2
    ans[level].append(arr[i])
    tree(start, i-1, level+1)
    tree(i+1, end, level+1)

tree(0, len(arr)-1, 0)

for x in ans:
    print(*x)