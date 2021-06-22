function solution(n) {
  var answer = -1;
  if (n ** (0.5) === parseInt(n ** (0.5))) {
    answer = (Number(n ** (0.5)+1) ** 2)
  }
  return answer;
}