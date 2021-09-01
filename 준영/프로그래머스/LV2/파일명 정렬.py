def solution(files):
    answer = []

    sort_files = [['', '', -1] for _ in range(len(files))]

    for i in range(len(files)):

        sort_files[i][2] = i

        for j in range(len(files[i])):
            if files[i][j].isdigit():
                sort_files[i][0] = files[i][:j].upper()
                sort_files[i][1] = files[i][j:]
                break

        for j in range(len(sort_files[i][1])):
            if not sort_files[i][1][j].isdigit():
                sort_files[i][1] = sort_files[i][1][:j]
                break

        
        sort_files[i][1] = int(sort_files[i][1])
    sort_files.sort(key= lambda x: (x[0], x[1]))
            
    for sort_file in sort_files:
        answer.append(files[sort_file[2]])

    return answer

files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)
files = ["img000012345", "img1.png","img2","IMG02"]
solution(files)