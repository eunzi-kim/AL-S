def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += ' '
            continue

        if ord(i) >= 97 and ord(i) <= 122:
            to_ord = (ord(i) - ord('a') + n) % 26
            to_ord += ord('a')
        
        if ord(i) >= 65 and ord(i) <= 90:
            to_ord = (ord(i) - ord('A') + n) % 26
            to_ord += ord('A')

        answer += chr(to_ord)

    return answer

print(ord('a'), ord('z'),ord('A'), ord('Z'))