def solution(n, m, section):
    answer = 0
    
    first = section.pop(0)
    while section:
        if section[0] - first < m:
            section.pop(0)
        else:
            first = section.pop(0)
            answer += 1

    answer += 1
    return answer

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))