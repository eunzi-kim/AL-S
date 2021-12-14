import sys
from collections import deque 

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[0]*M for _ in range(N)]

board = []

for _ in range(N):
  board.append(list(map(int, input().rstrip())))

def bfs(cnt, x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  q = []
  q.append((cnt, x, y))
  visited[x][y] = 1
  
  while q:
    cnt, x, y = q.pop(0)
    for i in range(len(dx)):
      n_x = x + dx[i]
      n_y = y + dy[i]
      n_cnt = cnt+1

      if 0 <= n_x <N and 0 <= n_y < M and board[n_x][n_y] ==1 and visited[n_x][n_y] ==0:
        if n_x == N-1 and n_y == M-1:
          return n_cnt
          
        q.append((n_cnt, n_x, n_y))
        visited[n_x][n_y] = 1

 

print(bfs(1, 0, 0))

