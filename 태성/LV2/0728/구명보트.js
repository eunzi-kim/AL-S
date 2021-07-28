const people = [10,20,30,40,50,60,70,80,90]
const limit = 100

function solution(people, limit) {
    var answer = people.length
    var cnt = 0
    var chk = Array.from({length:people.length}, (v, i)=>(0))
    console.log(chk)
    for (let j=0; j<people.length-1; j++) {
        if (chk[j] !==1) {
            let v = limit - people[j]
            chk[j] = 1
            
            let max_v = 0
            let max_v_i = 0
            for (let i=j+1; i<people.length; i++) {
                if (people[i] <= v && max_v<people[i] && chk[i]!==1) {
                    max_v = people[i]
                    max_v_i = i
                }
            }
            if (max_v !==0) {
                chk[max_v_i] = 1
                answer --
            }
            
        }
    }
    return answer
}

console.log(solution(people, limit))