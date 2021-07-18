var str1 = 'aa1+aa2'
var str2 = 'AAAA12'

function mk_arr(str1) {
    var arr = []
    for (let i=0; i<str1.length-1; i++) {
        function isAlpha(str) {
            var pattern = /^[a-zA-Z]+$/;
            return (pattern.test(str)) ? true : false;
        }
        // console.log(isAlpha(str1[i]))
        // console.log(isAlpha(str1[i+1]))
        
        if (isAlpha(str1[i])===true && isAlpha(str1[i+1])===true) {
            arr.push(str1[i].toUpperCase()+str1[i+1].toUpperCase())

        }
    }
    return arr
}

function solution(str1, str2) {
    var answer = 0
    console.log(mk_arr(str1))
    console.log(mk_arr(str2))
    // var str1_arr_h = mk_arr(str1)
    // var str2_arr_h = mk_arr(str2)

    var str1_arr = mk_arr(str1)
    var str2_arr = mk_arr(str2)
    var str1_n = str1_arr.length
    var str2_n = str2_arr.length
    if (str1_n.length === 0 && str2_n.length === 0) {
        return 65536
    }
    var gyo = []
    for (let s1 of str1_arr) {
        for (let i=0; i<str2_arr.length; i++) {
            if (s1 === str2_arr[i]) {
                var a = str2_arr[i]
                gyo.push(a)
                str2_arr.splice(i,1)
                break
            }
        }
    }
    console.log(gyo)
    console.log(gyo.length)
    
    
    var hap = str1_n + str2_n - gyo.length

    if (hap === 0) {
        return 65536
    }
    
    answer = parseInt((gyo.length/hap)*65536)
    
    return answer
}

console.log(solution(str1, str2))