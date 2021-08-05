def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.upper()
        if cacheSize == 0:
            answer += 5
        else:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                answer += 5
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
    return answer

cach = 2
c = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cach, c))