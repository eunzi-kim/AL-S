function solution(arr)
{
    var answer = [];
    var pre = -1
    for (let x of arr) {
      if (pre !== x) {
        answer.push(x)
        pre = x
      }
    }    
    return answer;
}