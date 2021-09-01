function solution(bridge_length, weight, truck_weights) {
  var answer = 0;
  var truck_time = [];
  for (let t_w of truck_weights) {
    truck_time.push([bridge_length, t_w])
  }

  var now = [];
  var now_weight = 0
  while (truck_time.length) {
    answer += 1

    var i=0
    while (i < now.length) {
      now[i][0] -= 1
      if (now[i][0] === 0) {
        now_weight -= now[i][1]
        now.splice(i, 1)
      } else {
        i += 1
      }
    }

    if (now_weight + truck_time[0][1] <= weight) {
      var v = truck_time.shift()
      now.push(v)
      now_weight += v[1]
    }
  }

  while (now.length) {
    answer += 1
    var j=0
    while (j<now.length) {
      now[j][0] -= 1
      if (now[j][0] === 0) {
        now_weight -= now[j][1]
        now.splice(j, 1)
      } else {
        j += 1
      }
    }
  }
  return answer;
}