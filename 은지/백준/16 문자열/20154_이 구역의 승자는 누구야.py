from copy import deepcopy

info = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

S = input()

arr = []
for v in S:
    arr.append(info[ord(v)-65])

temp = []
while len(arr) > 1:
    for i in range(1, len(arr), 2):
        temp.append((arr[i-1]+arr[i])%10)
    if len(arr) % 2:
        temp.append(arr[-1])
    arr = deepcopy(temp)
    temp = []

if arr[0] % 2:
    print("I'm a winner!")
else:
    print("You're the winner?")