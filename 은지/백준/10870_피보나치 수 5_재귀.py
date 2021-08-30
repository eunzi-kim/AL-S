n = int(input())

def fibo(x):
    if x == 0:
        return 0
    elif x == 1 or x ==2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(n))