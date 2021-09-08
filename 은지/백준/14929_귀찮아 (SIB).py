import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 자신까지의 누적합 배열
temp = [arr[0]]
for i in range(1, n):
    temp.append(temp[i-1]+arr[i])

# a*b+a*c=a*(b+c)를 이용
# 자신의 값 * 자신 이후의 누적합
ans = 0
for i in range(n-1):
    ans += arr[i] * (temp[n-1]-temp[i])  # 전체 누적합 - 자신까지의 누적합

print(ans)