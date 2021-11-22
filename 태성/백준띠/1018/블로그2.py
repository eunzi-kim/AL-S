import sys

input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

def chk(X):
  max_v = 0
  pre = 0
  for i in range(len(arr)-X+1):
    # print(arr[i:i+X])
    s_v = 0
    for k in range(i, i+X):
      s_v += arr[k]
    # s_v = sum(arr[i:i+X])
    if max_v < s_v:
      max_v = s_v
      pre = 1
    elif max_v == s_v:
      pre += 1

    
  if max_v == 0:
    print("SAD")
  else:
    print(max_v, end="\n")
    print(pre)

chk(X)

# 아니 왜 틀린지 모르겠소!!!!!!
  
