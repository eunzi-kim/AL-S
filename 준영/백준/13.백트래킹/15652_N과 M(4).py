N, M = map(int, input().split())

result = []
my_dic = {}

def my_func(arr, cnt, x):
    if cnt == M:
        result.append(arr)
    else:
        for i in range(x, N+1):
            my_func(arr+[i], cnt+1, i)

my_func([], 0, 1)
for i in result:
    print(*i)