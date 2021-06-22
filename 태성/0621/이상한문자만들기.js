const s = "try   hello world"	

function solution(s) {
    var answer = '';
    var ss = s.split(' ')
    console.log(ss)
    for (let sss of ss) {
        var pre = ''
        for (let i in sss) {
            
            if (i % 2 === 0) {
                pre += sss[i].toUpperCase()
            } else {
                pre += sss[i].toLowerCase()
            }
        }
        answer += pre
        answer += ' '
    }
    answer = answer.substring(0, answer.length-1)
    return answer;
}

console.log(solution(s))