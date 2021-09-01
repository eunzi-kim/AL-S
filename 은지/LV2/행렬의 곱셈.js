function solution(arr1, arr2) {
  var answer = [];
  for (let i=0; i<arr1.length; i++) {
    var sub_arr = []
    for (let k=0; k<arr2[0].length; k++) {
      var sub_v = 0
      for (let j=0; j<arr1[0].length; j++) {
        sub_v += arr1[i][j] * arr2[j][k]
      }
      sub_arr.push(sub_v)
    }
    answer.push(sub_arr)
  }
  return answer;
}