# n, k = map(int, input().split())

# arr = [i for i in range(1, n+1)]
# result = []
# idx = 0
# temp_n = 1

# while arr:
#     idx = idx % len(arr) 

#     if temp_n == k:
#         result.append(arr.pop(idx))
#         temp_n = 1
#         continue

#     idx += 1
#     temp_n += 1

# print('<' + ', '.join(map(str, result)) + '>')



n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
result = []
idx = 0

while arr:
    idx = (idx + k - 1) % len(arr)
    result.append(arr.pop(idx))

print('<' + ', '.join(map(str, result)) + '>')


