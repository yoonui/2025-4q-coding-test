def solution(numbers):
    arr = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            arr.append(numbers[i] + numbers[j])
    
    answer = list(set(arr))
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))