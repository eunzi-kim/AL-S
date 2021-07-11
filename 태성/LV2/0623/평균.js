function solution(arr) {
    var answer = 0;
    for(let a of arr) {
        answer += a
    }
    answer = answer / arr.length
    return answer;
}