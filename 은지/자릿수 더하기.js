function solution(n)
{
    var answer = 0;
    for (let x=n; n>0; x=x) {
      answer += n % 10
      n = parseInt(n/10)
    }
    return answer;
}