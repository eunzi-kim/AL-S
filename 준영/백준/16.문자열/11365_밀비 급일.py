temp = ''
arr = []

while True:
    temp = input()
    if temp == 'END': break
    back = ''
    N = len(temp)
    for i in range(N-1, -1, -1):
        back += temp[i]
    arr.append(back)

for i in arr:
    print(i)