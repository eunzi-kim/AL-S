import sys
input = sys.stdin.readline

N, X = map(int, input().split())

arr = [0] + list(map(int, input().split()))

arr_s = [0]*(N+1)

arr_s[1] = sum(arr[1:1+X])
# print(arr_s)
for i in range(2, len(arr)-(X-1)):
  arr_s[i] = arr_s[i-1] - arr[i-1] + arr[i+(X-1)]
# print(arr)
# print(arr_s)
# print(max(arr_s))

def ans(arr_s):
  max_v = max(arr_s)
  if max_v == 0:
    print("SAD")
    return 
  else:
    cnt = 0
    for k in arr_s:
      if k == max_v:
        cnt += 1

    print(max_v)
    print(cnt)
    return

ans(arr_s)

# print(arr)
