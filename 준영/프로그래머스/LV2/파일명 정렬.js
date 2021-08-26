function solution(files) {
  var answer = []

  var sort_files = Array.from({length: files.length}, () => Array(3).fill(''))
  
  for (let i = 0; i < files.length; i++) {
    sort_files[i][2] = i

    for (let j = 0; j < files[i].length; j++) {
      if (!isNaN(files[i][j])) {
        sort_files[i][0] = files[i].substr(0, j)
        sort_files[i][1] = files[i].substr(j)
        break
      }
    }

    for (let j = 0; j < sort_files[i][1].length; j++) {
      
      if (isNaN(sort_files[i][1][j])) {
        sort_files[i][1] = sort_files[i][1].substr(0, j)
        break
      }
    }
    
    sort_files[i][0] = sort_files[i][0].toUpperCase()
    sort_files[i][1] = parseInt(sort_files[i][1])
  }
  
  sort_files.sort((a, b) => {
    if (a[0] > b[0]) return 1
    else if (a[0] < b[0]) return -1
    else if (a[1] > b[1]) return 1
    else if (a[1] < b[1]) return -1
  })
  
  for (const sort_file of sort_files) {
    answer.push(files[sort_file[2]])
  }
  console.log(answer)
  return answer
}

files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)
files = ["img000012345", "img1.png","img2","IMG02"]
solution(files)
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
solution(files)