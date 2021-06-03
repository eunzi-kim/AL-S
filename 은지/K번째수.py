def solution(array, commands):
    answer = []
    for j in range(len(commands)):
        # array 배열 자르기
        subA = []
        for i in range(len(array)):
            subA = array[commands[j][0]-1:commands[j][1]]
        # 자른 배열 정렬
        subA.sort()
        # commands에서 언급한 연산 결과
        answer.append(subA[commands[j][2]-1])
    return answer