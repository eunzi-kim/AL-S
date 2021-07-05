# 💡 Level 1

### 모의고사.js

- JavaScript에서 최대값을 구할 때, `Math.max()`이용

- 리스트에서 최대값을 구하기 위해서 `Math.max(...List)`이용

  ```javascript
  const check = [1, 2, 3]
  const maxV = Math.max(...check) // maxV === 3
  ```

  

참고 : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math/max



### K번째수.js

- JavaScript에서 `sort()`는 문자열 기준으로 정렬!

- 숫자를 정렬할 때, 어떻게 정렬할지 기입

  ```javascript
  List.sort((a, b) => a-b)
  ```



### 폰켓몬.js

- python에서의 `in`과 JavaScript에서의 `includes`는 비슷한 기능!!

  ```javascript
  if (!mon.includes(x)) {
        mon.push(x)
      }
  ```



### 소수 만들기.py

- 조합, 순열 등 `itertools`이용하여 쉽게 사용하자!!

  ```python
  from itertools import combination
  ```




### 신규 아이디 추천.js

- 배열의 마지막 인덱스를 arr[-1]로 알 수 없음 

   👉 마지막 인덱스 구해야함!

   ```javascript
   arr[arr.length-1]
   ```

- 배열 탐색할 때, indexOf 이용!

   ```javascript
   arr.indexOf(x) != -1 // arr에 들어있는 x만 추출
   ```

- slice로 배열, 문자열 자를 수 있음

   ```javascript
   lst_a = lst_a.slice(0, 15)
   ```

- 배열 => 문자열 변환 : `arr.join(구분자)`

   ```javascript
   answer = lst_a.join('')
   ```



### 실패율.py

- 0으로 나누는 경우 런타임에러 발생!

  => 이 경우에 알맞은 조건 만들어주기!!

### 실패율.js

- 배열에 있는 요소 카운트 `filter`이용

  ```javascript
  let lv = stages.filter(ele => n+1 === ele).length
  ```

  👉 `stages`에 들어있는 `n+1`의 개수를 구할 수 있음

#### ⭐ 다음에 실패율 다시 한 번 풀어보기‼



### 3진법 뒤집기.js

- JavaScript에서 몫을 구할 때, `parseInt`이용!

  ```javascript
  paresInt(x/3) // x를 3으로 나눈 몫
  ```

- 10진법 -> 3진법 : 간단하게 `toString()`함수 이용!

  ```javascript
  n.toString(3) // n을 3진법으로 변경(문자열)
  ```



### 비밀지도.js

- 배열 초기화

  ```javascript
  // ex) n*m 배열 arr
  var arr = new Array(n)
  for (let i=0; i<m; i++) {
      arr[i] = new Array(n)
  }
  ```




### 다트 게임.js

- 배열의 합

  ```javascript
  const sum = array.reduce((a, b) => a+b, 0)
  ```

  👉 `Python`에서, `sum(array)`와 동일!!



### 제일 작은 수 제거하기.js

- `splice`함수

  : 배열 arr의 기존 요소를 삭제 또는 교체하거나 새 요소를 추가하여 배열 내용 변경

  ```javascript
  arr.splice(idx, 1)
  ```

  👉 배열 arr의 인덱스 idx부터 1개 삭제





# 💡 Level 2

### 124 나라의 숫자.js

- 배열의 역방향

  ```javascript
  arr.reverse()
  ```

  👉 배열 arr을 역방향으로 변경



### 오픈채팅방

- 띄어쓰기가 있는 문자열 => `split()`함수 이용‼



### 문자열 압축.js

- for문 이용

  ```javascript
  for (let i=0; i<n; i+=x) {}
  ```

  👉 `i`를 `x`번 더하는 반복



### 가장 큰 수.js

- 문자열 반복 함수 `String.repeat(n)`이용

  ```javascript
  "kleague".repeat(3)  // kleaguekleaguekleague 
  ```

  
