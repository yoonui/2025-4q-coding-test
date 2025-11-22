def solution(d, budget):
    answer = 0
    d.sort()

    for i in d:
        if budget - i >= 0:
            answer += 1
            budget -= i
        else: return answer

    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))