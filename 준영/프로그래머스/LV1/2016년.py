# 16년 1월 1일이 금요일
def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = ''
    result = 0
    for i in range(a-1):
        result += month[i]
    
    result += b
    answer = week[(result-1)%7]
    
    return answer

solution(5, 24)