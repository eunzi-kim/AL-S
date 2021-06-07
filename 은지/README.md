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