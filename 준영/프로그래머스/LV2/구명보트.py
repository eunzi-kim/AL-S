def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start = 0
    end = len(people) - 1

    while start < end:
        sum_boat = people[start] + people[end]
        if sum_boat > limit:
            start += 1
        else:
            start += 1
            end -= 1
        answer += 1

    if start == end: answer += 1
    
    return answer
