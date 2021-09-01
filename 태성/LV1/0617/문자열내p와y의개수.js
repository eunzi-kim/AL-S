function solution(s){
    var answer = true;

    var ss = s.toLowerCase()
    
    var sss = ss.split('')
    // console.log(sss)
    var p = sss.filter(e => 'p'===e).length
    // console.log(p)
    var y = sss.filter(e => 'y'===e).length
    
    if (p!==y) {
        answer = false
    }

    return answer;
}