function solution(s) {
    var answer = '';
    s = s.split('')
    var ss = s.sort((a, b) => a < b ? 1 : a > b ? -1: 0)
    ss = ss.join('')
    
    answer = ss
    return answer;
}