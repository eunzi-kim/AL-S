def solution(n):
    answer = ''
    role = ['4', '1', '2']
    arr = []
    while n:
        temp = n % 3
        arr.insert(0, role[temp])
        n //= 3 
        if temp == 0:
            n -= 1
    answer = ''.join(arr)
    return answer

# solution(1)
# solution(2)
solution(3)
# solution(4)
# solution(5)
# solution(6)
# solution(7)
# solution(8)
# solution(9)
# solution(10)