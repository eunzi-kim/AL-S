function solution(m, musicinfos) {
  var answer = '(None)'
  var max_play = 0

  const my_note = []

  for (let i = 0; i < m.length; i++) {
    if (m[i] == '#') {
      continue
    }

    if (i < m.length - 1) {
      if (m[i+1] == '#') {
        my_note.push(m[i]+m[i+1])
      } else {
        my_note.push(m[i])
      }
    } else {
      my_note.push(m[i])
    }
  }

  for (const music of musicinfos) {
    const temp = music.split(',')

    var [hour1, minute1] = [...temp[0].split(':').map(Number)]
    var [hour2, minute2] = [...temp[1].split(':').map(Number)]
    var total_minute1 = hour1 * 60 + minute1
    var total_minute2 = hour2 * 60 + minute2

    if (total_minute1 > total_minute2) {
      var gap = 24 * 60 - total_minute1 + total_minute2
    } else {
      var gap = total_minute2 - total_minute1
    }

    const note = []
    
    for (let i = 0; i < temp[3].length; i++) {
      if (temp[3][i] == '#') {
        continue
      }
      
      if (i < temp[3].length - 1) {
        if (temp[3][i+1] == '#') {
          note.push(temp[3][i]+temp[3][i+1])
        } else {
          note.push(temp[3][i])
        }
      } else {
        note.push(temp[3][i])
      }
    }

    var idx = 0
    var result = false
    var my_idx = 0

    while (idx < gap) {
      var real_idx = idx % note.length

      if (note[real_idx] == my_note[my_idx]) {
        while (note[real_idx] == my_note[my_idx]) {
          my_idx += 1
          real_idx += 1
          real_idx %= note.length
          if (my_idx == my_note.length) {
            result = true
            break
          }
        }
      }
      my_idx = 0

      idx += 1
    }

    if (result) {
      if (max_play < gap) {
        answer = temp[2]
        max_play = gap
      }
    }
  }


  return answer
}

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
solution(m, musicinfos)