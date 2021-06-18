const arr = [5, 9, 7, 10]	

const divisor = 5

function solution(arr, divisor) {
    var answer = []
    
    for (let a of arr) {
        if (a % divisor === 0) {
            answer.push(a)
        }
    }
    
    if (answer.length === 0) {
        answer.push(-1)
       
    }
    answer = answer.sort(function(a, b) {
  return a - b;
});
    console.log(answer)
    return answer
}

console.log(solution(arr, divisor))