function solution(s) {
    var answer = true;
    var tmp = parseInt(s)
    
    if ((s.length ==4 || s.length == 6) && s== tmp) {
        answer = true
    } else {
        answer = false
        
    }
    

    
    return answer;
}