N = int(input())

under_seven = [1, -1, 1, 2, -1]
up_eight = [2, 3, 2, 3, 4]

if N < 8:
    print(under_seven[N-3])
else:
    print(up_eight[(N-3)%5] + (N-8)//5)