import sys

input = sys.stdin.readline

arr = input().rstrip()
n = int(arr)

state = 0
def chk(a):
  pre = str(a)
  for p in pre:
    a += int(p)
  return a
# print(n)
for a in range(0, n+1):
  if n == chk(a):
    print(a)
    state = 1
    break

if state == 0:
  print(0)
  

