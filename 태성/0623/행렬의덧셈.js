function solution(arr1, arr2) {
    var answer = [];
    
    for (let i_1 in arr1){
        var pre = []
        for (let i_2 in arr1[i_1]){
            pre.push(arr1[i_1][i_2]+arr2[i_1][i_2])
            
        }
        answer.push(pre)
    }
    return answer;
}