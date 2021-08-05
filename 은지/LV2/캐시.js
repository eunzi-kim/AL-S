function solution(cacheSize, cities) {
  var answer = 0;
  var cache = [];
  for (let city of cities) {
    city = city.toUpperCase()
    if (cacheSize === 0) {
      answer += 5
    } else {
      if (cache.includes(city)) {
        answer += 1
        var i = cache.indexOf(city)
        cache.splice(i, 1)
        cache.push(city)
      } else {
        answer += 5
        if (cache.length < cacheSize) {
          cache.push(city)
        } else {
          cache.shift()
          cache.push(city)
        }
      }
    }
  }
  return answer;
}

cach = 3
c = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
console.log(solution(cach, c))