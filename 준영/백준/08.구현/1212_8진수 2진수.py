# import sys
# input = sys.stdin.readline

# N = input().rstrip()

# idx = 0
# ten = 0
# for i in range(len(N)-1, -1, -1):
#     ten += int(N[i]) * (8 ** idx)
#     idx += 1

# result = ''
# while ten:
#     result = str(ten % 2) + result
#     ten //= 2
    
# print(result)

print(bin(int(input(), 8))[2:])
