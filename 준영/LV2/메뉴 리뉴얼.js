function getAllCombinations(arr, m) {
  const combinations = []
  const picked = []
  const used = []
  for (const item of arr) used.push(0)

  function find(picked) {
    if (picked.length === m) {
      const rst = []
      for (let i of picked) {
        rst.push(arr[i])
      }
      combinations.push(rst)
      return
    } else {
      let start = picked.length ? picked[picked.length-1] + 1 : 0
      for (let i = start; i < arr.length; i++) {
        if (i === 0 || arr[i] !== arr[i-1] || used[i-1]) {
          picked.push(i)
          used[i] = 1
          find(picked)
          picked.pop()
          used[i] = 0
        }
      }
    }
  }
  find(picked)
  return combinations
}

function solution(orders, course) {
  var answer = []
  var comb_dict = {}
  for (const order of orders) {
    var temp = order.split('')
    temp.sort()

    for (const c of course) {
      var comb_list = getAllCombinations(temp, c)
      for (const comb of comb_list) {
        if (comb.join('') in comb_dict) {
          comb_dict[comb.join('')] = comb_dict[comb.join('')] + 1
        } else {
          comb_dict[comb.join('')] = 1
        }
      }
    }
  }
  var arr = []
  for (const comb in comb_dict) {
    arr.push([comb, comb_dict[comb]])
  }
  
  for (const i of course) {
    var max_i = 2
    var temp = []
    for (const j of arr) {
      if (j[0].length === i) {
        if (max_i < j[1]) {
          max_i = j[1]
          temp = [j[0]]
        } else if (max_i === j[1]) {
          temp.push(j[0])
        }
      }
    }
    for (const k of temp) {
      answer.push(k)
    }
  }
  answer.sort()
  return answer
}

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
console.log(solution(orders, course))
// orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
// course = [2, 3, 5]
// console.log(solution(orders, course))
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
console.log(solution(orders, course))