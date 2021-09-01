function permutation(arr, selectNum) {
  let result = [];
  if (selectNum === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    const fixer = v;
    const restArr = arr.filter((_, index) => index !== idx);
    const permuationArr = permutation(restArr, selectNum - 1);
    const combineFixer = permuationArr.map((v) => [fixer, ...v]);
    result.push(...combineFixer);
  });
  return result;
}

function is_prime(n) {
  var m = parseInt(n ** 0.5) + 1
  for (let i = 2; i < m; i++) {
    if (n % i === 0) return false
  }
  return true
}

function solution(numbers) {
  var answer = 0
  var result_arr = []
  var arr = numbers.split("")
  for (let i = 1; i <= arr.length; i++) {
    var arr_list = permutation(arr, i)
    for (const temp of arr_list) {
      var temp_n = parseInt(temp.join(""))
      if (temp_n === 0 || temp_n === 1) {
        continue
      }
      if (is_prime(temp_n)) {
        if (result_arr.includes(temp_n)) {
          continue
        } else {
          result_arr.push(temp_n)
        }
      }
    }
  }
  console.log(result_arr)
  answer = result_arr.length
  return answer
} 

solution("17")
solution("110")
solution("1234")