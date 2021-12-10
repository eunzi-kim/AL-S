import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ans = "YES"

    n = int(input())
    arr = [input().rstrip() for _ in range(n)] 
    arr.sort()    

    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            ans = "NO"
            break

    print(ans)