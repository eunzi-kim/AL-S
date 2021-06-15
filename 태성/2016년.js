const a = 5
const b = 24

const board = [
  [],
  ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"],
  ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
  ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"],
  ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"],
  ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"],
  ["TUE", "WED", "THU", "FRI", "SAT", "SUN", "MON"],
  ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"],
  ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"],
  ["WED", "THU", "FRI", "SAT", "SUN", "MON", "TUE"],
  ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"],
  ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"],
  ["WED", "THU", "FRI", "SAT", "SUN", "MON", "TUE"],
]

function solution(a, b) {
  var answer = '';
  var value = b % 7
  answer = board[a][value]
  return answer;
}

console.log(solution(a, b))

// 아 윤년을 나중에 확인했어 ㅅㅂ ...