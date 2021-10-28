import sys
input = sys.stdin.readline

k = int(input())

def search(k, cnt):
    n = 0
    while 2**(n+1) <= k:
        n += 1

    if n == 0:
        if cnt % 2 == 0:
            return k
        else:
            if k == 1:
                return 0
            else:
                return 1
    else:
        return search(k-(2**n), cnt+1)

print(search(k-1, 0))