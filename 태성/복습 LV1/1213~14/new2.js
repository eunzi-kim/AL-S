function solution(new_id) {
    var answer = ''
    //1
    answer = new_id.toLowerCase()
    
    //2
    let str_arr = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    var answer2 = ''
    for (let i=0; i<answer.length; i++ ) {
        if (str_arr.includes(answer[i])) {
            answer2 += answer[i]
        }
    }
    
    //3
    let answer3 = ''
    let pre = ''
    for (let i=0; i<answer2.length; i++) {
        if (answer2[i] === '.') {
            pre += '.'
        } else {
            if (pre.length !== 0) {
                answer3 += '.'
                pre = ''
                // console.log(answer3)
            }
            answer3 += answer2[i]
            // console.log(answer3)
        }
    }
    if (pre.length !== 0) {
        answer3 += '.'
        pre = ''
    }

    //4
    // console.log(answer3)
    if (answer3[0] === '.') {
        answer3 = answer3.slice(1)
    }
    if (answer3[answer3.length-1] === '.') {
        answer3 = answer3.slice(0, answer3.length-1)
    }
    // console.log(answer3)

    //5
    if (answer3.length === 0) {
        answer3 = 'a'
    }

    //6
    if (answer3.length >= 16) {
        answer3 = answer3.slice(0, 15)
    }
    console.log("여기")
    console.log(answer3)
    if (answer3[answer3.length-1] === '.') {
        answer3 = answer3.slice(0, answer3.length-1)
    }
    console.log(answer3)

    //7
    if (answer3.length <= 2) {
        let n = 3 - answer3.length
        for (let i=0; i<n; i++) {
            answer3 += answer3[answer3.length-1]
        }
    }

    return answer3
}
let new_id = "abcdefghijklmn.p"
console.log(solution(new_id))