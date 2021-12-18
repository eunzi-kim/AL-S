N = int(input())
city_length = list(map(int, input().split()))  # N-1
price = list(map(int, input().split()))  # N

ans = price[0] * city_length[0]
temp = price[0]
for i in range(1, N-1):
    temp = min(temp, price[i])
    ans += temp * city_length[i]

print(ans)