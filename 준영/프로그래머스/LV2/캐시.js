function solution(cacheSize, cities) {
  var answer = 0
  const city_cache = []

  for (const city of cities) {
    if (cacheSize === 0) {
      answer = 5 * cities.length
      break
    }

    var new_city = city.toLowerCase()

    if (!city_cache.includes(new_city)) {
      if (city_cache.length < cacheSize) {
        city_cache.push(new_city)
      } else {
        city_cache.shift()
        city_cache.push(new_city)
      }
      answer += 5
    } else {
      const n = city_cache.indexOf(new_city)
      city_cache.splice(n, 1)
      city_cache.push(new_city)
      answer += 1
    }
    
  }
  return answer
}