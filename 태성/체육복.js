const n = 5
const lost = [2, 3, 4]
const reserve = [1, 3, 5]

function solution(n, lost, reserve) {
    // var answer = 0;
    for (let i in lost){
        for (let j in reserve){
            if (lost[i] === reserve[j]){
                lost.splice(i, 1)
                reserve.splice(j, 1)
            }
        }
    }
    // console.log(lost)

    // console.log(n_lost)
    for (let i of reserve) {
        let key = lost.includes(i-1) ? lost.indexOf(i-1) : lost.indexOf(i+1)
        if (key != -1) {
            lost.splice(key, 1)
        }
    }
    console.log(lost)
    
    return n-lost.length;
}

console.log(solution(n, lost, reserve))