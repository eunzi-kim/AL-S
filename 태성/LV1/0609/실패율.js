const N = 4
const stages = [4,4,4,4,4]	

function solution(N, stages) {
    var answer = []

    var lost_arr = []

    var top = []
    var bottom = []

    for (let i=0; i<N; i++) {
        top.push(0)
        bottom.push(0)
    }
    // console.log(top)

    for (let s of stages) {
        if(s > N) {
            for (let i in bottom) {
                bottom[i] ++
            }
        } else {
            for (let ii=0; ii<s; ii++) {
                bottom[ii] ++

            }
            top[s-1] ++
        }
    }
    console.log(top)
    console.log(bottom)

    for (let i in top) {
        if (bottom[i] === 0) {
            lost_arr.push([0, parseInt(i)+1])
        } else {
            lost_arr.push([top[i] / bottom[i], parseInt(i)+1])
        }
    }
    console.log(lost_arr)
    console.log(lost_arr.sort((a, b) => {return b[0]-a[0]}))

    console.log(lost_arr)
    for (let la of lost_arr) {
        answer.push(la[1])
    }

    return answer
}

console.log(solution(N, stages))