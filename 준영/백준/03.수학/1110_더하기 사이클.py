N = input()

temp = N
cnt = 0
while True:
    cnt += 1
    if len(temp) > 1:
        temp = str(int(temp[-1] + str(int(temp[0]) + int(temp[1]))[-1]))
    else:
        temp = str(int(temp[-1] + str(0 + int(temp[0]))[-1]))
    
    if temp == N:
        break
print(cnt)