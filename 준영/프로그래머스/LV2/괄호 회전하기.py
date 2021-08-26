def solution(s):
    answer = 0
    temp = s
    for i in range(len(s)):
        my_stack = []
        is_right = True
        for j in temp:
            if j == '[' or j == '{' or j == '(':
                my_stack.append(j)
            
            if j == ']': 
                if len(my_stack) == 0:
                    is_right = False
                    break
                if my_stack[-1] == '[':
                    my_stack.pop()
                else:
                    is_right = False
            
            if j == '}':
                if len(my_stack) == 0:
                    is_right = False
                    break
                if my_stack[-1] == '{':
                    my_stack.pop()
                else:
                    is_right = False
            
            if j == ')':
                if len(my_stack) == 0:
                    is_right = False
                    break
                if my_stack[-1] == '(':
                    my_stack.pop()
                else:
                    is_right = False
        if len(my_stack):
            is_right = False
            
        if is_right:
            answer += 1

        temp = temp[1:] + temp[0]
    
    return answer

s = "[](){}"	
solution(s)