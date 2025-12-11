def solution(number, limit, power):
    div = []

    for i in range(1, number+1):
        num = 0
        for j in range(1, int(i**(1/2)+1)):
            if i % j == 0:
                if i // j == j:
                    num += 1
                else: num += 2
        div.append(num)

    answer = 0
    for i in div:
        if i <= limit: answer += i
        else: answer += power
    return answer

print(solution(5, 3, 2))
print(solution(10, 3, 2))