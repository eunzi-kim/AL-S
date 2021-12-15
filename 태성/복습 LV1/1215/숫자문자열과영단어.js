function solution(s) {
    var answer = ''
    n_list = '1234567890'
    pre = ''
    for (let i=0; i<s.length; i++) {
        if (n_list.includes(s[i])) {
            // console.log(s[i])
            if (pre.length !== 0) {
                if (pre === 'zero') {
                    answer += '0'
                    pre = ''
                } else if (pre === 'one') {
                    answer += '1'
                    pre = ''
                } else if (pre === 'two') {
                    answer += '2'
                    pre = ''
                } else if (pre === 'three') {
                    answer += '3'
                    pre = ''
                } else if (pre === 'four') {
                    answer += '4'
                    pre = ''
                } else if (pre === 'five') {
                    answer += '5'
                    pre = ''
                } else if (pre === 'six') {
                    answer += '6'
                    pre = ''
                } else if (pre === 'seven') {
                    answer += '7'
                    pre = ''
                } else if (pre === 'eight') {
                    answer += '8'
                    pre = ''
                } else if (pre === 'nine') {
                    answer += '9'
                    pre = ''
                } 
            }
            answer += s[i]
        } else {
            pre += s[i]
        }

        if (pre === 'zero') {
            answer += '0'
            pre = ''
        } else if (pre === 'one') {
            answer += '1'
            pre = ''
        } else if (pre === 'two') {
            answer += '2'
            pre = ''
        } else if (pre === 'three') {
            answer += '3'
            pre = ''
        } else if (pre === 'four') {
            answer += '4'
            pre = ''
        } else if (pre === 'five') {
            answer += '5'
            pre = ''
        } else if (pre === 'six') {
            answer += '6'
            pre = ''
        } else if (pre === 'seven') {
            answer += '7'
            pre = ''
        } else if (pre === 'eight') {
            answer += '8'
            pre = ''
        } else if (pre === 'nine') {
            answer += '9'
            pre = ''
        } 
        
        // pre += s[i]
    }
    return answer;
}


let s = "23four5six7"
console.log(solution(s))