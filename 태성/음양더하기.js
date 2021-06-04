function solution(absolutes, signs) {
    var answer = 0
    
    for (let i=0; i<signs.length; i++) {
        if(signs[i] === true) {
            signs[i] = 1
        } else {
            signs[i] = -1
        }
    }
    
    for (let i=0; i<signs.length; i++) {
        answer += absolutes[i]*signs[i]
    }
    return answer
}