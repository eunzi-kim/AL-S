const clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	

function solution(clothes) {
    var answer = 0
    var ojt = {}

    for (let i=0; i<clothes.length; i++) {
        if (clothes[i][1] in ojt === true) {
            ojt[clothes[i][1]] ++
        } else {
            ojt[clothes[i][1]] = 1
        }
    }
    console.log(ojt)
    // for (let i=0; i<ojt.length; i++) {
    //     console.log(ojt[i])
    // }
    // console.log(ojt[0])
    const arr = Object.values(ojt)
    console.log(arr)
    answer = 1
    for (let a of arr) {
        answer *= a +1
    }
    return answer -1
}

console.log(solution(clothes))