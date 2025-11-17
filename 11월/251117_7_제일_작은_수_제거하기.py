def solution(arr):
    answer = []
    num = min(arr)

    for i in arr:
        if i != num: answer.append(i)

    return [-1] if len(answer) == 0 else answer

print(solution([4,3,2,1]))
print(solution([10, 10 , 10]))