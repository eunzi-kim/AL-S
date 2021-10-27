import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
chk = list(map(int, input().split()))

arr.sort()


def search(x, s, e):
    if s > e:
        return 0

    mid = (s+e)//2

    if x == arr[mid]:
        return 1

    if x < arr[mid]:
        return search(x, s, mid-1)
    elif x > arr[mid]:
        return search(x, mid+1, e)


ans = ""
for x in chk:
    ans += str(search(x, 0, N-1)) + " "

print(ans)