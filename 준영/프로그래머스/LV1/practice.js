function solution(s){
  var answer = true;

  var ss = s.toLowerCase()
  ss = Array(ss)
  console.log(ss)
  
  var arr = ss.filter(e => 'p'===e)
  
  console.log(arr)
  return answer;
}

solution('ppYY')