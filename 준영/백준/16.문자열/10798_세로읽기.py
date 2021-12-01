arr = []
for i in range(5):
    arr.append(input())

result = ''
idx = 0

while True:
    end = 0
    for i in range(len(arr)):
        if len(arr[i]) > idx:
            result += arr[i][idx]
        else:
            end += 1

    if end == len(arr):
        break
    idx += 1

print(result)

