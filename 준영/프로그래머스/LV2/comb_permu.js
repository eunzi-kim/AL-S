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

