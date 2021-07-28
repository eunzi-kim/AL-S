var people = [70, 50, 80, 50]	
const limit = 100


function solution(people, limit) {
    var answer = people.length
    people.sort(function(a, b) {return b - a})
    console.log(people)
    let i = 0
    let j = people.length-1
    while (i < j) {
        if (people[i] + people[j] <= limit) {
            answer --
            i ++
            j --
        } else {
            i ++
        }
    }
    return answer
}

console.log(solution(people, limit))