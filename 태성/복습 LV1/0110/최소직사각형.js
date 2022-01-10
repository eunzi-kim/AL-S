function solution(sizes) {
    var answer = 0;
    let left = []
    let right = []
    for (let i=0; i<sizes.length; i++) {
        if (sizes[i][0] > sizes[i][1]) {
            left.push(sizes[i][0])
            right.push(sizes[i][1])
        } else {
            right.push(sizes[i][0])
            left.push(sizes[i][1])
        }
    }
    // console.log(pre)
    // console.log(Math.max(left))
    answer = Math.max(...left) * Math.max(...right)
    return answer;
}

let sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	

console.log(solution(sizes))

