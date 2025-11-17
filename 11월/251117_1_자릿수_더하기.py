def solution(n):
    num = n
    answer = 0

    for i in range(len(str(n))):
        answer += num % 10
        num = num // 10
        
    return answer

print(solution(123))
print(solution(987))