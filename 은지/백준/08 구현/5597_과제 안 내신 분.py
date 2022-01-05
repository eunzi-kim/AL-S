chk = [0] * 31
chk[0] = 1

for _ in range(28):
    x = int(input())
    chk[x] = 1

for i in range(1, 31):
    if chk[i] == 0:
        print(i)