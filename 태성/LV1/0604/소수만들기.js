const nums = [1,2,3,4]

let pre = []

for (let i=0; i<(nums.length-2); i++) {
    for (let j=i+1; j<(nums.length-1); j++){
        for (let k=j+1; k<(nums.length); k++){
            // console.log(nums[i])
            // console.log(nums[j])
            // console.log(nums[k])
            pre.push(nums[i] + nums[j] + nums[k])
            // console.log(pre)
        }
    }
}
// console.log(pre)
let chk = []

for (let p of pre) {
    for (let i=2; i<(p/2)+1; i++){
        if (p%i === 0){
            chk.push(p)
            break
        }
    }
}
// console.log(pre.length)
// console.log(chk.length)

answer = pre.length - chk.length

console.log(answer)