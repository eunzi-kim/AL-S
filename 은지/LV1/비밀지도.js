function solution(n, arr1, arr2) {
  var answer = [];
  // 지도 초기화
  var map = new Array(n)
  for (let i=0; i<n; i++) {
    map[i] = new Array(n)
  }
  for (let i=0; i<n; i++) {
    // 10진수 => 2진수
    var a1 = arr1[i].toString(2)
    var a2 = arr2[i].toString(2)
    // 벽 입력
    for (let j=a1.length-1; j>=0; j--) {
      map[i][j+n-a1.length] = Number(a1[j])   
    }
    for (let j=a2.length-1; j>=0; j--) {
      if (map[i][j+n-a2.length] >= 0) {
        map[i][j+n-a2.length] += Number(a2[j])
      } else {
      map[i][j+n-a2.length] = Number(a2[j])
      }      
    }
  }
  // 지도 출력
  for (let i=0; i<n; i++) {
    var result = ""
    for (let j=0; j<n; j++) {
      if (map[i][j]) {
        result += "#"
      } else {
        result += " "
      }
    }
    answer.push(result)
  }
  return answer;
}