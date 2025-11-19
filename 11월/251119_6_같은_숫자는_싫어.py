def solution(arr):
    answer = []
    last = -1
    
    for i in arr:
        if i != last:
            answer.append(i)
            last = i

    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))