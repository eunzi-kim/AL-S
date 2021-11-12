N = int(input())

road = list(map(int, input().split()))
gas_station = list(map(int, input().split()))

min_gas = int(1e9)
sum_gas = 0

for i in range(N-1):
    if gas_station[i] < min_gas:
        min_gas = gas_station[i]

    sum_gas += min_gas * road[i]

print(sum_gas)