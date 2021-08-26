def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    new_word = ""
    for n in new_id:
        asc = ord(n)
        if asc == 45 or asc == 95 or asc == 46:
            new_word += n
        elif asc >= 48 and asc <= 57:
            new_word += n
        elif asc >= 97 and asc <= 122:
            new_word += n
    
    # 3
    new_word_3rd = ""
    idx = 0
    for n in new_word:
        if n == '.':
            idx += 1
        elif n != '.' and idx != 0:
            new_word_3rd += "."
            new_word_3rd += n
            idx = 0
        else:
            new_word_3rd += n

    # 4
    new_word = new_word_3rd.strip('.')


    # 5
    if len(new_word) == 0:
        new_word = "a"

    # 6
    if len(new_word) >= 16:
        new_word = new_word[:15]

    new_word = new_word.strip('.')

    # 7
    x = new_word[-1]
    while len(new_word) < 3:
        new_word += x
    
    answer = new_word
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"	
print(solution(new_id))
new_id = "z-+.^."	
print(solution(new_id))
new_id = "=.="
print(solution(new_id))
new_id = "123_.def"
print(solution(new_id))
new_id = "abcdefghijklmn.p"	
print(solution(new_id))