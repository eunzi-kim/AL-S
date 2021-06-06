arr = [1, 2, 3]

const new_set = new Set(arr)

console.log(new_set)

const new_arr = new Array(new_set)
const new_arr2 = new Array(...new_set)

console.log(new_arr)
console.log(new_arr2)