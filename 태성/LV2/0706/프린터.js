function solution(priorities, location) {
    var answer = 0
    var arr = []
    for (let i=0; i<priorities.length; i++) {
        arr.push(i)
    }
    var cnt = 0
    var j = 0
    while (true) {
        var p = priorities.shift()
        // console.log(p)
        j = arr.shift()
        var pp = priorities.filter(a => a>p)
        if (pp.length!==0) {
            priorities.push(p)
            arr.push(j)
        } else {
            cnt ++
            if (j===location) {
                answer = cnt
                break
            }
        }
    }


    return answer
}