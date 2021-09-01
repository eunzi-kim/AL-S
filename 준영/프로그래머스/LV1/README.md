# 💡 21.06.024

### 소수 만들기.js

- 해당 문제를 풀기위해서는 3개의 숫자를 뽑는 조합이 필요했다.
- 조합을 만들기 위해 재귀로 조합을 만드는 방법을 택하였다.

```javascript
const getCombinations = function (arr, selectNumber) {
  const results = []
  
  if (selectNumber === 1) return arr.map((value) => [value])
    
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1)
    const combinations = getCombinations(rest, selectNumber - 1)
    const attached = combinations.map((combination) => [fixed, ...combination])
    
    results.push(...attached)
  })

  return results
}
```

- 배열에서 하나를 앞에서부터 한개씩 선택하고 그 이후의 배열을 재귀로 호출, 나머지 배열에서 1개를 줄인 조합을 만든다.

