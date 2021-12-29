function solution(N, stages) {
    var answer = [];

    let arr_cnt = []
    let arr_suc = []
    for (let i=0; i<N+2; i++) {
        arr_cnt.push(0)
        arr_suc.push(0)
    }
    
    
    for (let i=0; i<stages.length; i++) {
        let n = stages[i]
        arr_cnt[n] ++
        // console.log(arr_cnt)
        for (let j=1; j<n+1; j++) {
            arr_suc[j] ++
            // console.log(arr_suc)
        }
    }
    console.log("check")
    console.log(arr_cnt)
    console.log(arr_suc)

    let fail = []
    for (let i=1; i<N+1; i++) {
        if (arr_suc[i] === 0 && arr_cnt[i] !==0) {
            fail.push(1)
        } else if (arr_suc[i] === 0 && arr_cnt[i] ===0) {
            fail.push(0)
        } else {
            fail.push(arr_cnt[i]/arr_suc[i])
        }
    }
    console.log(fail)
    let dict = {}
    for (let i=0; i<fail.length; i++) {
        dict[i+1] = fail[i]
    }
    console.log(dict)

    let items = Object.keys(dict).map(function(key) {
        return [key, dict[key]];
    });

    items.sort(function(first, second) {
        return second[1] - first[1];
    });

    console.log(items)

    for (let i=0; i<items.length; i++) {
        answer.push(parseInt(items[i][0]))
    }
    console.log(answer)

    return answer;
}
let N = 5
let stages = [4,4,4,4,4]		
solution(N, stages)