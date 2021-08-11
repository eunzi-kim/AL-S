a = [1, 2]
b = [a, [2, 3]]

console.log(b.includes([2, 3]))

a = [1, 2]
b = [[1, 2], [2, 3]]

console.log(b.includes(a))