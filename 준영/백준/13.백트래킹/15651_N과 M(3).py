N, M = map(int, input().split())

result = []
def my_func(arr, cnt):
    if cnt == M:
        result.append(arr)
    else:
        for i in range(1, N+1):
            my_func(arr+[i], cnt+1)

my_func([], 0)
for i in result:
    print(*i)