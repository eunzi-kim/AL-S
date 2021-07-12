function solution(str1, str2) {
  var answer = 0
  
  var myRegExp = /[A-Z]{2}/
  var re_str1 = str1.toUpperCase()
  var re_str2 = str2.toUpperCase()

  var re_str1_dict = {}
  var re_str2_dict = {}

  for (let i = 0; i < re_str1.length-1 ; i++) {
    if (myRegExp.test(re_str1.slice(i, i+2))) {
      if (re_str1.slice(i, i+2) in re_str1_dict) {
        re_str1_dict[re_str1.slice(i, i+2)] = re_str1_dict[re_str1.slice(i, i+2)] + 1
      } else {
        re_str1_dict[re_str1.slice(i, i+2)] = 1
      }
    }
  }

  for (let i = 0; i < re_str2.length-1 ; i++) {
    if (myRegExp.test(re_str2.slice(i, i+2))) {
      if (re_str2.slice(i, i+2) in re_str2_dict) {
        re_str2_dict[re_str2.slice(i, i+2)] = re_str2_dict[re_str2.slice(i, i+2)] + 1
      } else {
        re_str2_dict[re_str2.slice(i, i+2)] = 1
      }
    }
  }

  var re_str_max = {}
  var re_str_min = {}

  for (const key in re_str1_dict) {
    if (key in re_str2_dict) {
      re_str_max[key] = Math.max(re_str1_dict[key], re_str2_dict[key])
      re_str_min[key] = Math.min(re_str1_dict[key], re_str2_dict[key])
    } else {
      re_str_max[key] = re_str1_dict[key]
    }
  }

  for (const key in re_str2_dict) {
    if (key in re_str1_dict) {
      re_str_max[key] = Math.max(re_str1_dict[key], re_str2_dict[key])
    } else {
      re_str_max[key] = re_str2_dict[key]
    }
  }

  var max_val = 0
  var min_val = 0

  for (const key in re_str_max) {
    max_val += re_str_max[key]
  }
  
  for (const key in re_str_min) {
    min_val += re_str_min[key]
  }

  if (max_val === 0) {
    answer = 65536
  } else {
    answer = 65536 * (min_val / max_val)
    answer = Math.floor(answer)
  }

  return answer
}