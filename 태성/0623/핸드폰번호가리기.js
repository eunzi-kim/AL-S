phone_number = "01033334444"	

function solution(phone_number) {
    var answer = '';

    // console.log(phone_number[0:3])
    // console.log(phone_number)

    var arr = phone_number.slice(-4)
    // console.log(arr)

    var pre_arr = ''
    for (let i= 0; i<phone_number.length-4; i++) {
        pre_arr += '*'
    }
    // console.log(pre_arr)
    
    answer = pre_arr + arr
    return answer;
}

solution(phone_number)