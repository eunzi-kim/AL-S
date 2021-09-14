import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trie = {}

for i in range(N):
    s = input().rstrip()
    trie[s] = True

result = 0

for i in range(M):
    t = input().rstrip()
    if trie.get(t):
        result += 1

print(result)