var s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"								

function solution(s) {
    var answer = [];
    s = s.substring(1,s.length-1)

    console.log(s)
    var pre = []
    for (let ss of s) {
        if (ss === '{') {
            var cnt_ = 0
            var tmp = ''
        } else if (ss === ',') {
            cnt_ ++
            tmp = tmp + ss
        } else if (ss === '}') {
            cnt_ ++
            pre.push([cnt_, tmp])
        } else {
            tmp = tmp + ss
        }
    }
    console.log(pre)
    pre.sort(function(a, b){
        return a[0] - b[0]
    })
    console.log(pre)
    // var arr = Array.from({length: 1000000}, () => 0)
    // console.log(arr)

    var tmp = []
    for (let p of pre) {
        var pre_tmp = ''
        for (let pp of p[1]) {
            if (pp === ',') {
                if(tmp.includes(pre_tmp)===false) {
                    tmp.push(pre_tmp)
                    pre_tmp = ''
                    break
                } else {
                    pre_tmp = ''
                }
            } else{
                pre_tmp = pre_tmp + pp
            }
        }
        if (pre_tmp.length !==0 && tmp.includes(pre_tmp)===false) {
            tmp.push(pre_tmp)
        }
    }
    console.log(tmp)
    for (let t of tmp) {
        answer.push(parseInt(t))
    }
    console.log(answer)

    return answer;
}


solution(s)