def solution(want, number, discount):

    dit = {}
    for i in range(len(want)):
        dit[want[i]] = number[i]

    answer = 0
    for i in range(len(discount)-9):
        tmp = discount[i : i+10]
        for j in dit:
            if tmp.count(j) != dit[j]: break
            if j == want[-1]:
                answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1] , ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))