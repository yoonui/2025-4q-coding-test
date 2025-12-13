def solution(k, tangerine):
    answer = 0
    dit = {}
    
    for i in tangerine:
        if i in dit: dit[i] = dit[i] + 1
        else: dit[i] = 1
    
    arr = list(dit.values())
    arr.sort()

    while k > 0:
        num = arr.pop()
        k -= num
        answer+=1

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))