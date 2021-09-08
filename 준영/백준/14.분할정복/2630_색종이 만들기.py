import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

blue = 0
white = 0

def is_all(arr):
    global blue
    global white

    n = len(arr)
    x = arr[0][0]
    result = True

    for i in range(n):
        if arr[i].count(x) != n:
            result = False
    
    if result:
        if x == 1:
            blue += 1
        else:
            white += 1
    else:
        temp = []
        for i in range(n//2):
            temp_x = []
            for j in range(n//2):
                temp_x.append(arr[i][j])
            temp.append(temp_x)
        is_all(temp)

        temp = []
        for i in range(n//2, n):
            temp_x = []
            for j in range(n//2):
                temp_x.append(arr[i][j])
            temp.append(temp_x)
        is_all(temp)

        temp = []
        for i in range(n//2):
            temp_x = []
            for j in range(n//2, n):
                temp_x.append(arr[i][j])
            temp.append(temp_x)
        is_all(temp)

        temp = []
        for i in range(n//2, n):
            temp_x = []
            for j in range(n//2, n):
                temp_x.append(arr[i][j])
            temp.append(temp_x)
        is_all(temp)
                
is_all(arr)

print(white)
print(blue)
