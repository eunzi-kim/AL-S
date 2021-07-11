function solution(array, commands) {
    var answer = [];
    for (let i=0; i<commands.length; i++) {
        let n_array = commands[i]
        let d = n_array[0]
        let j = n_array[1]
        let k = n_array[2]
        
        let pre_array = array.slice(d-1, j)
        let a_array = pre_array.sort((a,b) => a-b)
        
        answer.push(a_array[k-1])
    }
    
    return answer;
}