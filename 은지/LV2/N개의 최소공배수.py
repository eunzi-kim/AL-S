def solution(arr):
    while len(arr) > 1:
        a = arr.pop(0)
        b = arr.pop(0)
        v = min(a, b)
        gcd = v
        for x in range(1, v+1):
            if a % x == 0 and b % x == 0:
                gcd = x
        arr.append((a*b)//gcd)
    return arr[0]