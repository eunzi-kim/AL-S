N, M = map(int, input().split())
pocket_mon = [input() for _ in range(N)] # 포켓몬 이름 배열
pocket_num = {} # 포켓몬 {이름: 번호}

for i in range(N):
    pocket_num[pocket_mon[i]] = i+1

info = [input() for _ in range(M)]

for x in info:
    if x.isnumeric():
        print(pocket_mon[int(x)-1])
    else:
        print(pocket_num[x])