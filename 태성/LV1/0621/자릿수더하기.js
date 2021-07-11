const n = 123

function solution(n)
{
    var answer = 0;

    var s_n = n.toString()
    // console.log(s_n)
    for (let s of s_n) {
        answer += parseInt(s)
    }

    return answer;
}


console.log(solution(n))