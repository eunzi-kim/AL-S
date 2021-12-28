function solution(answers) {
    var ans = [];
    let arr = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    let answers_len = answers.length
    let pre_ans = []
    for (let i=0; i<arr.length; i++) {
        let pre_arr = arr[i]
        let pre = []
        let p_a_l = pre_arr.length
        if (answers_len > p_a_l) {
            var moc = Math.floor(answers_len/p_a_l)
            var namuzi = answers_len - (p_a_l* moc)
        } else {
            var moc = Math.floor(p_a_l/answers_len)
            var namuzi = p_a_l - (answers_len* moc)
        }

        // let namuzi = answers_len - (p_a_l* moc)
        console.log(pre_arr)
        console.log(moc, namuzi)
        for (let a=0; a<moc; a++) {
            for (let b=0; b<p_a_l; b++) {
                pre.push(pre_arr[b])
                // console.log(pre)
            }
        }
        if (namuzi !== 0) {
            for (let b=0; b<namuzi; b++) {
                pre.push(pre_arr[b])
            }
        }
        console.log("pre")
        console.log(pre)
        let cnt = 0
        for (let j=0; j<answers_len; j++) {
            if (answers[j] === pre[j]) {
                cnt ++
            }
        }
        pre_ans.push(cnt)
        // console.log("cnt")
        // console.log(cnt)
        // console.log(moc, namuzi)
    }
    console.log(pre_ans)
    // let idx = []
    let max = 0
    for (let i=0; i<pre_ans.length; i++) {
        if (pre_ans[i]>max) {
            max = pre_ans[i]
            ans = [i+1]
        } else if (pre_ans[i] ===max) {
            ans.push(i+1)
        }
    }

    return ans;
}
let answers = [1,3,2,4,2]	
console.log(solution(answers))