function solution(nums) {
    var answer = 0;
    let set_nums = new Set(nums)
    let n_nums = [...set_nums]
    
    if (n_nums.length > nums.length/2){
        answer = nums.length/2
    } else {
        answer = n_nums.length
    }
    return answer;
}