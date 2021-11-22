N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 1
my_dic = {}
result = 0
my_dic[arr[0]] = 1

while True:
    x = arr[start]
    y = arr[end]
    
    if my_dic.get(y):
        if my_dic[y] < K:
            my_dic[y] += 1
            if result < end - start + 1:
                result = end - start + 1
            end += 1
        else:
            my_dic[x] -= 1
            start += 1
    else:
        if result < end - start + 1:
            result = end - start + 1
        my_dic[y] = 1
        end += 1
    if end >= N:
        break
    
print(result)
