import sys
input = sys.stdin.readline

N = int(input())
card_dict = {}
for i in list(map(int, input().split())):
    card_dict[i] = '1'

M = int(input())
cards = list(map(int, input().split()))
result = []
for i in cards:
    if card_dict.get(i):
        result.append(1)
    else:
        result.append(0)
print(*result)

