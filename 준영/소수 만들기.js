const isPrime = function (nums) {
  const sumNums = nums.reduce((sum, i) => {
    return sum + i
  }, 0)
  var i = 2
  while (i < sumNums) {
    if (sumNums % i === 0) {
      return false
    }
    i += 1
  }
  return true
}

const getCombinations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1); // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = getCombinations(rest, selectNumber - 1); // 나머지에 대해서 조합을 구한다.
    const attached = combinations.map((combination) => [fixed, ...combination]); //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    results.push(...attached); // 배열 spread syntax 로 모두다 push
  });

  return results; // 결과 담긴 results return
}

function solution(nums) {
  var answer = 0
  const results = getCombinations(nums, 3)
  for (const result of results) {
    if (isPrime(result)) {
      answer += 1
    }
  }
  return answer;
}

nums = [1, 2, 3, 4]
console.log(solution(nums))