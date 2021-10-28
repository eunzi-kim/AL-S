N = int(input())

def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2:
        return 1-recursive(n//2)
    else:
        return recursive(n//2)
print(recursive(N-1))

0
0 1
0 1 1 0
0 1 1 0 1 0 0 1
0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0

1 0
2 1
3 1
4 0

5 1
6 0
7 0
8 1

9 1 
10 0
11 0
12 1

13 0
14 1
15 1
16 0

0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1
