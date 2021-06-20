const s = "AaZz"
const n = 25


const arr1 = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 65))

// console.log(arr1)
const arr3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'w', 't', 'u', 'v', 'w', 'x', 'y', 'z']

// console.log(arr3)

function solution(s, n) {
    // var n_split = n.split('')
    var answer = '';
    for (let nn of s) {
        if (nn === ' ') {
            answer += ' '
        }
        for (let i_1=0; i_1<arr1.length; i_1++)  {
            if (nn === arr1[i_1]) {
                n_1 = (i_1+n) % 26
                answer += arr1[n_1]
            }
        }

        for (let i_2=0; i_2<arr3.length; i_2++) {
            if (nn === arr3[i_2]) {
                n_2 = (i_2+n) % 26
                answer += arr3[n_2]
            }
        }
            
    }


    return answer;
}

console.log(solution(s, n))