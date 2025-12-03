def solution(k, score):
    answer = []
    tmp = []

    for i in score:
        tmp.append(i)
        tmp.sort(reverse=True)
        tmp = tmp[:k]
        answer.append(tmp[-1])

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))