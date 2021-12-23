function solution(numbers) {
    var answer = 0;
    const arr = [1,2,3,4,5,6,7,8,9,0]
    for (let i=0; i<arr.length; i++) {
        if (numbers.includes(arr[i]) === true) {
            // console.log(numbers[i])
            continue
        } else {
            answer += arr[i]
        }
    }
    return answer;
}

numbers = [1,2,3,4,6,7,8,0]
console.log(solution(numbers))