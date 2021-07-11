var n = 8
var a = 4
var b = 7

function solution(n,a,b){
    var answer = 0;

    while (a!==b) {
        a = Math.ceil(a/2)
        b = Math.ceil(b/2)

        answer ++
    }

    return answer;
}

console.log(solution(n,a,b))