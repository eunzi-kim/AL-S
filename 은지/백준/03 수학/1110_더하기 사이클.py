N = input()

num = N
cnt = 0
while True:
    if int(num) < 10:
        num = "0" + num

    temp = 0
    for x in num:
        temp += int(x)
    cnt += 1
    num = num[-1]+str(temp)[-1]

    if int(num) == int(N):
        break

print(cnt)