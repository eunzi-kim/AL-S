import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

arr = []

def search(s, e):
    if s > e:
        return

    x = arr[s]
    idx = s + 1

    for i in range(s+1, e+1):
        if arr[i] > x:
            idx = i
            break
    
    search(s+1, idx-1)
    search(idx, e)

    print(x)


while True:
    try:
        arr.append(int(input()))
    except:
        break

n = len(arr)   

search(0, n-1)