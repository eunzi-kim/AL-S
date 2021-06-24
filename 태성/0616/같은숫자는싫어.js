const arr = [1,1,3,3,0,1,1]	

function solution(arr){
    var answer = [];

    var pre = arr[0]
    for (i=1; i<arr.length; i++) {
      if (pre === arr[i]) {
        pre = arr[i]
      } else {
        answer.push(pre)
        pre = arr[i]
      }

    }

    answer.push(pre)
    
    return answer;
}

console.log(solution(arr))