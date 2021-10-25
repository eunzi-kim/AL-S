N, B = input().split()

B = int(B)

result = 0

idx = 0

for i in range(len(N)-1, -1, -1):
    if N[i].isdigit():
        result += (B ** idx) * int(N[i])
    else:
        result += (B ** idx) * (ord(N[i]) - 55)

    idx += 1

print(result)