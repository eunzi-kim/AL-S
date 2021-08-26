def solution(cacheSize, cities):
    answer = 0

    city_cache = []

    for city in cities:
        if cacheSize == 0:
            answer = 5 * len(cities)
            break

        if city.lower() not in city_cache:
            if len(city_cache) < cacheSize:
                city_cache.append(city.lower())
            else:
                city_cache.pop(0)
                city_cache.append(city.lower())    
            answer += 5
        else:
            n = city_cache.index(city.lower())
            city_cache.pop(n)
            city_cache.append(city.lower())    
            
            answer += 1
    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
solution(cacheSize, cities)
