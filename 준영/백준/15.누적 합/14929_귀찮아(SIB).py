import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr2 = arr[:]

adding = 0
for i in range(N-1,-1,-1):
    adding += arr[i]
    arr2[i] = adding


result = 0
for i in range(N-1):
    result += (arr[i] * arr2[i+1])

print(result)