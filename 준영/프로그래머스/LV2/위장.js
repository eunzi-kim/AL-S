function solution(clothes) {
  var answer = 1
  var clothes_dict = {}

  for (const c of clothes) {
    var cloth = c[0]
    var cate = c[1]
    
    
    if (!(cate in clothes_dict)) {
      clothes_dict[cate] = [cloth]
    } else {
      clothes_dict[cate].push(cloth)
    }
  }
  for (const key in clothes_dict) {
    var n = clothes_dict[key].length
    answer *= (n + 1)
  }
  return answer - 1
}

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)