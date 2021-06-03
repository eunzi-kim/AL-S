const n = 5
const lost = [2, 3, 4]
const reserve = [1, 3, 5]

function solution(n, lost, reserve) {
    var answer = 0;
    // console.log(reserve)
    for (const l of lost) {
        console.log(lost)
        console.log(l)
        if (reserve.indexOf(l) !== -1){
            lost.shift()
            reserve.splice(reserve.indexOf(l), 1)
            // console.log(l)
        }else{
            if (reserve.indexOf(l-1) !== -1){
                lost.shift()
                reserve.splice(reserve.indexOf(l-1), 1)
                // console.log(lost)
            } else if (reserve.indexOf(l+1) !== -1){
                    lost.shift()
                    reserve.splice(reserve.indexOf(l+1), 1)
            }
        }
    }
    // console.log(lost)
    // console.log(lost.length)
    return answer;
}

solution(n, lost, reserve)

// if (reserve.indexOf(l) !== -1){
//     lost.shift()
//     reserve.splice(reserve.indexOf(l), 1)
//     console.log(l)
// }else{
//     if (reserve.indexOf(l-1) !== -1){
//         lost.shift()
//         reserve.splice(reserve.indexOf(l-1), 1)
//         // console.log(lost)
//     } else if (reserve.indexOf(l+1) !== -1){
//             lost.shift()
//             reserve.splice(reserve.indexOf(l+1), 1)
//     }
// }
// }