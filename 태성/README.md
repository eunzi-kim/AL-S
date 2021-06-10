## 신규아이디추천.js

```
테스트케이스 6, 18, 26 실패
-> 질문 작성
```

## 0608키패드

### 키패드.py

- 36분 37초 (첫번째 시도)

### 키패드.js

```
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/in

=> in 은 인덱스 및 속성값을 이용;; 특이 

=>include를 사용
```



## 0609실패율

### 실패율.py

- 1, 6, 7, 9, 23, 24, 25 => 런타임 에러..

```
다중 sort 때문에 개고생 많이 함 ..

직접 다중 sort 시도 ... => 실패...

now_tal = pre[0][0]
same_tal_stage = []
for i in pre:
    if now_tal != i[0]:
        same_tal_stage.sort()
        answer.extend(same_tal_stage)
        same_tal_stage = []

        now_tal = i[0]
        same_tal_stage.append(i[1])
    else:
        same_tal_stage.append(i[1])
same_tal_stage.sort()
answer.extend(same_tal_stage)
```

```
다중 sort (직접 지정해주는 방법)
https://ooyoung.tistory.com/59

```

```
딕셔너리 sort

대부분의 정답들이 이걸 사용
```

![스크린샷 2021-06-09 20.12.25](/Users/leetaesung/Desktop/git/AL-S/AL-S/태성/static/스크린샷 2021-06-09 20.12.25.png)

=>버전에 따라 달라지는 활용..



=> 현재 교수님과 프로그래머스 질문하기에 올렸는데 존나 시발 아니 ㅈ같은게 틀린 이유나 답을 찾는 방법이 전무.. 아니 무슨 해답지가 없는 느낌 ... 개같다 진짜 

### 06103진법뒤집기
```
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
```
=> int에 10진법으로 만들어주는 기능이 있다니...!!!!!!!! 놀랍도다 파이떤!!!!!!!


### 빈번 실수

js에서 for문에 let 안넣음 ;;

거의 지금 세번째 실수 