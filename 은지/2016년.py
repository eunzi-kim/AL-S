def solution(a, b):
    Month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    # 일 수 더하기
    day = b-1
    # 달의 일 수 더하기
    for i in range(a-1):
        day += Month[i]
    # 변경 요일 탐색
    day %= 7
    answer = Week[day]
    return answer