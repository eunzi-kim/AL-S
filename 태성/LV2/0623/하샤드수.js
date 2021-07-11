function solution(x) {
    var answer = true;
    var x1 = x.toString()
    
    var pre = 0
    for (let xx of x1) {
        pre += parseInt(xx)
    }
    
    if (x/pre === parseInt(x/pre)){
        answer = true
    } else {
        answer = false
    }
    return answer;
}