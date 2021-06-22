const n = 12

function solution(n) {
    var answer = 0;

    var arr = []
    for (let i=1; i<n+1; i++) {
        arr.push(i)
    }

    for (let a of arr) {
        if (n % a === 0) {
            answer += a
        }
    }
    return answer
}

console.log(solution(n))