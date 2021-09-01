const n = 3

function solution(n) {
    var answer = 0;
    let sq = Math.sqrt(n)
    // console.log(sq)
    // console.log(Math.sqrt(n))
    // console.log(Math.pow(sq, 2))

    if (sq === parseInt(sq)) {
        answer = Math.pow(sq+1, 2)
    } else {
        answer = -1
    }
    return answer;
}

// 처음에 제곱근을 했을때 완전히 안떨어지는 숫자인 소수가 나오면 다시 제곱을 했을때 정수가 나오지 않는다고 판단...
// 근데 정수가 나오는 애들이 있었음 디버깅 불가 
// 그래서 다른 아이디어로 준영님이 알려주신 from을 활용해 일일히 비교하려 했는데 런타임에러 ...
// 결국 고심 끝에 parseInt로 비교하기로 정답.

console.log(solution(n))