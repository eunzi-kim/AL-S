def solution(n):
    answer = ''
    example = '수박'
    for x in range(n):
        answer += example[x%2]
    return answer