def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if len(citations)-i <= citations[i]:
            answer = len(citations)-i
            break
            
    return answer