const fs = require('fs'); 
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(v => +v);
n = input[0]
k = input[1]

var answer = "<"
var p = []
for (let x=1; x<=n; x++) {
  p.push(x)
}

var i = k-1
while (p.length > 1) {
  var v = p.splice(i, 1)
  i = (k+i-1) % p.length
  answer += String(v) + ", "
}
v = p.pop()
answer += String(v) + ">"

console.log(answer)