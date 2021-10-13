N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

result = 0

for i in range(N):
    if result < arr[i]*(i+1):
        result = arr[i]*(i+1)

print(result)
    