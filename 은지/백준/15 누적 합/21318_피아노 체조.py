import sys
input = sys.stdin.readline

N = int(input())
level = list(map(int, input().split()))

mistake = [0]*N
for i in range(N-1):
    if level[i] > level[i+1]:
        mistake[i+1] = mistake[i]+1
    else:
        mistake[i+1] = mistake[i]

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(mistake[y-1]-mistake[x-1])