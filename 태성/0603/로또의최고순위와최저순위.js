function solution(lottos, win_nums) {
    var answer = [];
    const dict = {
        0:6,
        1:6,
        2:5,
        3:4,
        4:3,
        5:2,
        6:1,
    }
    
    var max_cnt = 0
    for (let i=0; i<6; i++) {
        if (lottos[i] === 0) {
            max_cnt += 1
            
        } else{
            for(let j=0; j<6; j++) {
                if (lottos[i] === win_nums[j]) {
                    max_cnt += 1
                }
            }
        }
        
    }
    answer.push(dict[max_cnt])
    
    var min_cnt = 0
    for (let i=0; i<6; i++) {
        if (lottos[i] === 0) {
            
        } else{
            for(let j=0; j<6; j++) {
                if (lottos[i] === win_nums[j]) {
                    min_cnt += 1
                }
            }
        }
        
    }
    answer.push(dict[min_cnt])
    
    
    return answer;
}