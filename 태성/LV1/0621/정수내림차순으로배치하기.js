const n = 118372

function solution(n) {
    var answer = 0;
    var s_n = n.toString().split('')
    // console.log(s_n)
    var n_arr = []
    for (let s of s_n) {
        n_arr.push(parseInt(s))
    }

    // console.log(n_arr)

    n_arr.sort(function(a, b) { // 내림차순
        return b - a;
        // 11, 10, 4, 3, 2, 1
    })

    answer = n_arr
    return answer;
}

solution(n)