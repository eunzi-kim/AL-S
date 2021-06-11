function solution(left, right) {
    var answer = 0
    for (i=left; i<right+1; i++) {
        var cnt = 0
        for (a=1; a<i+1; a++) {
            if (i % a === 0) {
                cnt +=1
            }
        }

        if (cnt % 2 === 0) {
            answer += i
        } else {
            answer -= i
        }
    }

    return answer
}

console.log(solution(13, 17))