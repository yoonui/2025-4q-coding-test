def solution(s, n):
    answer = ''
    
    lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
    upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    for i in s:
        if i == ' ': answer+= i

        if i in lower:
            num = lower.index(i)+n
            answer += lower[num % 26]
        
        if i in upper:
            num = upper.index(i)+n
            answer += upper[num % 26]

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))