def solution(N, stages):
    failNum = {}
    stages.sort()
    userNum = len(stages)

    for i in range(1, N+1):
        if i in failNum: continue
        if i in stages:
            cnt = stages.count(i)
            failNum[i] = cnt / userNum
            userNum = userNum - cnt
        else:
            failNum[i] = 0

    answer = sorted(failNum, key=lambda x:failNum[x], reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))