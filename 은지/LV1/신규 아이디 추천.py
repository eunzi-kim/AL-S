def solution(new_id):
    answer = ''
    # 1단계
    id = new_id.lower()
    # 변경 아이디 담을 리스트 초기화
    lst_a = []
    # .의 개수 카운트
    cnt = 0
    for x in id:
        # 2단계
        if x == '-' or x == '_' or x == '.' or x.isalpha() or x.isnumeric():
            # 3단계
            if x == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt <= 1:
                lst_a.append(x)
    # 4단계
    if len(lst_a) > 0 and lst_a[0] == '.':
        lst_a.pop(0)
    if len(lst_a) > 0 and lst_a[-1] == '.':
        lst_a.pop(-1)
    # 5단계
    if len(lst_a) == 0:
        lst_a.append('a')
    # 6단계
    if len(lst_a) >= 16:
        lst_a = lst_a[:15]
        if len(lst_a) > 0 and lst_a[-1] == '.':
            lst_a.pop(-1)
    # 7단계
    if len(lst_a) == 1:
        lst_a.append(lst_a[-1])
        lst_a.append(lst_a[-1])
    elif len(lst_a) == 2:
        lst_a.append(lst_a[-1])
    # 리스트 => 문자열 변환
    answer = "".join(lst_a)
    return answer