import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
card = deque([x for x in range(1, N+1)])

while len(card) > 1:
    card.popleft()
    v = card.popleft()
    card.append(v)

print(card[0])