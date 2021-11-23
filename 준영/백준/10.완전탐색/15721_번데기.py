A = int(input())
T = int(input())
X = int(input())

arr = [0 for _ in range(A)]

idx = 0

temp = 0

cnt = 2

stop = True

while stop:
    for i in range(4):
        arr[idx] = i % 2

        if i%2 == X:
            temp += 1
            if temp == T:
                result = idx
                stop = False
                break    
            
        idx += 1
        if idx >= A:
            idx = 0

    for i in range(cnt):
        if X == 0:
            temp += 1
            if temp == T:
                result = idx
                stop = False
                break    

        arr[idx] = 0
        idx += 1
        if idx >= A:
            idx = 0
    
    for i in range(cnt):
        if X == 1:
            temp += 1
            if temp == T:
                result = idx
                stop = False
                break    
        
        arr[idx] = 1
        idx += 1
        if idx >= A:
            idx = 0
    
    cnt += 1

print(result)