def solution(absolutes, signs):
    answer = 0
    n = len(absolutes)
    for i in range(n):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


absolutes = [4,7,12]
signs = [True,False,True]	
print(solution(absolutes, signs))


absolutes = [1,2,3]	
signs = [False,False,True]
print(solution(absolutes, signs))