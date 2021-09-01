var arr = [4,3,2,1]	


function solution(arr) {
    
    var min_v = Math.min.apply(null, arr)
    // (...arr)
    for (let i=0; i<arr.length; i++) {
        if (min_v === arr[i]) {
            arr.splice(i, 1)
            break
        }
    }
    if (arr.length === 0) {
        arr.push(-1)
    }
    return arr;
}

console.log(solution(arr))