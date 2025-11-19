def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6: 
        for i in s:
            if ord(i) > 64: return False
    else: return False

    return answer

print(solution('a234'))
print(solution('1234'))