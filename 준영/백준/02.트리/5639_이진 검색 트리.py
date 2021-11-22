import sys
sys.setrecursionlimit(10 ** 9)

def postorder(arr):
    length = len(arr)

    if length <= 1:
        return arr

    for i in range(1, length):
        if arr[i] > arr[0]:
            return postorder(arr[1:i]) + postorder(arr[i:]) + [arr[0]]

    return postorder(arr[1:]) + [arr[0]]

arr = []

while True:
    try:
        arr.append(int(input()))

    except:
        break

new_arr = postorder(arr)

for i in new_arr:
    print(i)