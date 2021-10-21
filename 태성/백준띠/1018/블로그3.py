import sys

input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

def chk(X):
  a = 0
  max_v = s_v = sum(arr[a:a+X])
  # print(max_v)
  cnt = 1

  for aa in range(a, len(arr)-X):
    s_v -= arr[aa]
    s_v += arr[aa+X]
    if max_v < s_v:
      max_v = s_v
    elif max_v == s_v:
      cnt += 1

  if max_v == 0:
    print("SAD")
    return
  else:
    print(max_v, end="\n")
    print(cnt)
    return

chk(X)
  
