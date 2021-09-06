N = int(input())

idx = 1
while True:
    if idx * (idx + 1) / 2 == N:
        print(idx)
        break
    elif idx * (idx + 1) / 2 > N:
        print(idx - 1)
        break

    idx += 1