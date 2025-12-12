def solution(s):
    arr = []
    
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if len(arr) <=0 : return False
            else: arr.pop()

    return True if len(arr) == 0 else False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))