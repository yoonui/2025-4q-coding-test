def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5]
    p1Num = 0
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p2Num = 0
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p3Num = 0

    ansLen = len(answers)
    for i in range(ansLen):
        if p1[i % len(p1)] == answers[i]: p1Num+=1
        if p2[i % len(p2)] == answers[i]: p2Num+=1
        if p3[i % len(p3)] == answers[i]: p3Num+=1

    maxNum = max([p1Num, p2Num, p3Num])
    if maxNum == p1Num: answer.append(1)
    if maxNum == p2Num: answer.append(2)
    if maxNum == p3Num: answer.append(3)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))