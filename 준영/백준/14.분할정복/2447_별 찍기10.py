N = int(input())

arr = [[' ' for _ in range(N)] for _ in range(N)]

def star(n, xs, ys):

    if n == 3:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    arr[i+xs][j+ys] = '*'

    else:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    star(n//3, xs+i*(n//3), ys+j*(n//3))

star(N, 0, 0)

for i in range(N):
    print(''.join(arr[i]))
