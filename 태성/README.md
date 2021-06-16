## 명예의 전당

- 0609실패율
- 



## 0601크레인.js

- 약 16분(0613)



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



=> 현재 교수님과 프로그래머스 질문하기에 올렸는데 존나 시발 아니 ㅈ같은게 틀린 이유나 답을 찾는 방법이 전무.. 아니 무슨 해답지가 없는 느낌 ... 개같다 진짜 => 은지짱을 통해 문제를 발견 0으로 나누는 예외가 발생

### 0613 복습

lambda를 이용한 sorted 함수의 실패로 풀이 실패 ㅠㅠ

```
https://ooyoung.tistory.com/59
```

### 실패율.js

```
python3에서 [0]*(N+1)이
JS에서는 안된다.

function mk_young_list(N) {
  var lst = []
  for (let i=0; i<(N+1); i++) {
    lst[i] = 0
  }
  return lst
}
```





##06103진법뒤집기 

### 3진법뒤집기.py 
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

### 3진법뒤집기.js
combination은 중복 for문으로 가능
js는 제로초님 블로그가 최고인듯 앞으로도 자주 참고
```
https://www.zerocho.com/category/JavaScript/post/5acafb05f24445001b8d796d
```
은지를 통해 알게 된 includes
그리고 reduce 함수를 공부하게 되어 좋았음
준영님을 통해 permutation 체크해서 다행..!

## 0614 2016년 -> 복습요망



## 06104비밀지도

### 비밀지도.py 

배열 뒤집기 세가지 방법

```
a = [1, 2, 3]
b = list(reversed(a))

print(b)

c = [1, 2, 3]

c.reverse()

print(c)

d = [1, 2, 3]
e = d[::-1]

print(e)
```

https://www.youtube.com/watch?v=sGhY8dQdu4A

##빈번 실수

- js에서 for문에 let 안넣음 ;;

=> 거의 지금 다섯번째 실수 



- python3와 js 사이의 다른 문법들 

  => in vs include