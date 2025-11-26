def solution(s):
    answer = []

    for i in range(len(s)):
        num = s[:i].rfind(s[i])
        if num == -1: answer.append(num)
        else: answer.append(i-num)
    return answer

print(solution('banana'))
print(solution('foobar'))