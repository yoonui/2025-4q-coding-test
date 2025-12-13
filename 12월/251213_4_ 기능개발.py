import math

def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        num = 100 - progresses[i]
        days.append(math.ceil(num / speeds[i]))

    tmp = []
    while len(days) > 0:
        first = days.pop(0)
        tmp.append(first)

        if len(days) == 0:
            answer.append(len(tmp))
            tmp = []
        elif max(tmp) < days[0]:
            answer.append(len(tmp))
            tmp = []

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([85, 80, 90, 85], [5, 5, 5, 5]))