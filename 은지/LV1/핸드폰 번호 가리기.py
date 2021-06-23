def solution(phone_number):
    answer = ''
    n = len(phone_number)
    answer = "*" * (n-5) + phone_number[n-5:]
    return answer