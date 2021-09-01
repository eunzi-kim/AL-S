def solution(phone_number):
    answer = ''
    n = len(phone_number)
    answer = "*" * (n-4) + phone_number[n-4:]
    return answer