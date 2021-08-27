import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_dict = {}
pokemon_arr = []
idx = 0

for i in range(N):
    name = input().rstrip()
    pokemon_dict[name] = idx
    pokemon_arr.append(name)
    idx += 1

for i in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(pokemon_arr[int(q)-1])
    else:
        print(pokemon_dict.get(q)+1)