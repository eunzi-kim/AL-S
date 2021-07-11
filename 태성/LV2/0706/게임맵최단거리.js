function bfs(n, m, maps) {
    // var v = Array.from({length:n}, (a)=>0).fill(0)
    // let visited = []

    // for (let i=0; i<m; i++) {
    //     visited.push(v)
    // }

    var visited = Array.from(Array(m), ()=> new Array(n).fill(0))

    // console.log(visited)

    var dx = [-1, 1, 0, 0]
    var dy = [0, 0, -1, 1]

    var Q = []
    Q.push([0, 0, 1])
    visited[0][0] = 1

    while (Q.length!==0) {
        var QQ = Q.shift()
        var x = QQ[0]
        var y = QQ[1]
        var cnt = QQ[2]

        for (let i=0; i<4; i++) {
            var n_x = x + dx[i]
            var n_y = y + dy[i]
            if (n_x === m-1 && n_y === n-1) {
                return cnt+1
            } 

            if (0<=n_x && n_x<m && 0<=n_y && n_y<n && visited[n_x][n_y]===0 && maps[n_x][n_y]===1) {
                Q.push([n_x, n_y, cnt+1])
                visited[n_x][n_y] = 1
            }



        }
    }

    return -1
}

var maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	

function solution(maps) {
    var answer = 0
    const m = maps.length
    const n = maps[0].length

    answer = bfs(n, m, maps)
    
    return answer
}

console.log(solution(maps))