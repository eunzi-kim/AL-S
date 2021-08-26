function sum_arr(arr) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  return arr.reduce(reducer)
}

function solution(bridge_length, weight, truck_weights) {
  const bridge_arr = new Array(bridge_length).fill(0)
  var N = truck_weights.length

  bridge_arr.shift()
  bridge_arr.push(truck_weights[0])
  
  var time = 1
  var idx = 1
  
  while (idx < N || sum_arr(bridge_arr) > 0) {
    time += 1
    bridge_arr.shift()
    if (idx >= N) {
      bridge_arr.push(0)
    } else {
      if (sum_arr(bridge_arr) + truck_weights[idx] <= weight) {
        bridge_arr.push(truck_weights[idx])
        idx += 1
      } else {
        bridge_arr.push(0)
      }
    }
  }

  return time
}

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)