function solution(num) {
    var answer = 0;
    var cnt = 0
    while (num != 1) {
        cnt += 1
        if (cnt >500) {
            return -1
        }
        
        if (num % 2 === 0) {
            num = num / 2 
        } else {
            num = num*3 +1
        }
    }
    return cnt;
}