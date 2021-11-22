N = int(input())
M = int(input())

zzang = [x for x in range(N)]


def search(x):
    if x == zzang[x]:
        return x

    zzang[x] = search(zzang[x])
    return zzang[x]


def change(a, b):
    zzang_a = search(a)
    zzang_b = search(b)

    if zzang_a < zzang_b:
        zzang[zzang_b] = zzang_a
    else:
        zzang[zzang_a] = zzang_b


for r in range(N):
    city_info = list(map(int, input().split()))
    for c in range(N):        
        if city_info[c]:
            change(r, c)

plan = list(map(int, input().split()))

root = []
for city in plan:
    if search(city-1) not in root:
        root.append(search(city-1))

if len(root) == 1:
    print("YES")
else:
    print("NO")