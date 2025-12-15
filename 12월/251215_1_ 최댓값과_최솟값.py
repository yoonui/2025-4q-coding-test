def solution(s):
    arr = list(s.split(" "))
    numArr = [int(x) for x in arr]

    tmp = []
    tmp.append(str(min(numArr)))
    tmp.append(str(max(numArr)))

    answer = ' '.join(tmp)
    return answer

# print(solution("1 2 3 4"))
# print(solution("-1 -2 -3 -4"))
# print(solution("-1 -1"))
print(solution("1000 123 12345"))