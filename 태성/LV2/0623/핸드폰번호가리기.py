
phone_number = "01033334444"

def solution(phone_number):
    answer = ''
    arr = phone_number[len(phone_number ) -4:len(phone_number)]

    pre_arr = ''.join(["*"]*(len(phone_number)-4))

    answer = pre_arr +arr
    return answer

print(solution(phone_number))



