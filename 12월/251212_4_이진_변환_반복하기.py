def solution(s):
    answer = [0, 0]
    num = int(s, 2)

    while num > 1:
        tmp = []
        for i in s:
            if i == '1': tmp.append(i)
            else: answer[1]+=1
        num = len(tmp)
        answer[0]+=1
        s = bin(num)[2:]

    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))