import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(N)]

def maketree(arr, rank):
    mid = (len(arr)//2)
    tree[rank].append(arr[mid])
    if len(arr) == 1:
        return
    maketree(arr[:mid], rank+1)
    maketree(arr[mid+1:], rank+1)

maketree(arr, 0)

for i in range(N):
    print(*tree[i])
