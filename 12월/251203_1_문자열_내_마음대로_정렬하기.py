def solution(strings, n):
    answer = []
    arr = []

    for i in strings:
        tmp = i[n] + i
        arr.append(tmp)
    arr.sort()

    for i in arr:
        answer.append(i[1:])

    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))