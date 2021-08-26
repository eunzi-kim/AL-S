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

function solution(expression) {
  var answer = 0

  var arr = []
  var temp_str = ''
  var x = []

  for (let i = 0; i < expression.length; i++) {
    if (expression[i] === '-' || expression[i] === '+' || expression[i] === '*') {
      arr.push(Number(temp_str))
      arr.push(expression[i])
      temp_str = ''
      if (!x.includes(expression[i])) {
        x.push(expression[i])
      }
    } else {
      temp_str += expression[i]
    }
  }
  arr.push(Number(temp_str))

  var x_list = permutation(x, x.length)
  const temp = []
  for (const x of x_list) {  
    temp.length = 0
    var arr1 = arr
    var skip = false
    console.log(temp)
    for (const i of x) {
      console.log(temp)
      for (let j = 0; j < arr1.length; j++) {
        if (skip) {
          skip = false
          continue
        }

        if (arr1[j] === i) {
          var temp_i = temp.pop()
          if (arr1[j] === '-') {
            temp.push(temp_i - arr1[j+1])
          } else if (arr1[j] === '+') {
            temp.push(temp_i + arr1[j+1])
          } else if (arr1[j] === '*') {
            temp.push(temp_i * arr1[j+1])
          }
          skip = true
        } else {
          temp.push(arr1[j])
        }
      }
    }

    if (temp.length === 1) {
      answer = Math.abs(temp[0]) > answer ? Math.abs(temp[0]) : answer
    } else {
      arr1 = temp
      temp.length = 0
    }
  }
  return answer
}

expression = "100-200*300-500+20"


console.log(solution(expression))