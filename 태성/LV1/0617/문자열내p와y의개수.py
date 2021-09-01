def solution(s):
    answer = True
    
    s = s.lower()
    
    
    a = s.count("p")
    b = s.count("y")
    
    if a != b :
        answer = False
            

    return answer