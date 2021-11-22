import copy
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

while len(arr) > 1:
    n = len(arr)
    temp = []
    for i in range(0, n, 2):
        x = []
        for j in range(0, n, 2):
            temp_arr = []
            for k in range(2):
                for t in range(2):
                    temp_arr.append(arr[i+k][j+t])                    
            temp_arr.sort(reverse=True)
            x.append(temp_arr[1])
        temp.append(x)
    arr = copy.deepcopy(temp)
print(arr[0][0])