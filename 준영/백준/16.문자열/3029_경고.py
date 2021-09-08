start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

result = 0
if start[0] > end[0]:
    result += 3600 * (24 + end[0] - start[0])
else:
    result += 3600 * (end[0] - start[0])

if start[1] > end[1]:
    if result < 60 * 60:
        result += 3600 * 24
    result -= 60 * 60
    result += 60 * (60 + end[1] - start[1])
else:
    result += 60 * (end[1] - start[1])

if start[2] > end[2]:
    if result < 60:
        result += 3600 * 24
    result -= 60
    result += (60 + end[2] - start[2])
else:
    result += (end[2] - start[2])
    
if result == 0:
    result = 3600 * 24

hour = result // 3600
result %= 3600
minute = result // 60
result %= 60
second = result

print(format(hour, '02'), format(minute, '02'), format(second, '02'), sep=':') 