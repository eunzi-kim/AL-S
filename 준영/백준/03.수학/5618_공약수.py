import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = []

for i in range(1, arr[0]+1):
    temp = 0
    for j in arr:
        if j % i == 0:
            temp += 1
        else:
            break
        
        if temp == N:
            result.append(i)
            temp = 0

for i in result:
    print(i)

