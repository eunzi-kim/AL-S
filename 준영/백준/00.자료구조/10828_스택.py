import sys
input = sys.stdin.readline

N = int(input())

arr = []

result = []

for _ in range(N):
    temp = list(input().split())

    if temp[0] == 'push':
        arr.append(temp[1])
    elif temp[0] == 'pop':
        if len(arr):
            x = arr.pop()
            result.append(x)
        else:
            result.append('-1')
    elif temp[0] == 'size':
        result.append(len(arr))
    elif temp[0] == 'empty':
        if len(arr):
            result.append('0')
        else:
            result.append('1')
    elif temp[0] == 'top':
        if len(arr):
            result.append(arr[-1])
        else:
            result.append('-1')

for i in result:
    print(i)
