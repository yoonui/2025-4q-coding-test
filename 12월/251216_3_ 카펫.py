def solution(brown, yellow):
    answer = []
    for i in range(1,int( yellow**(1/2))+1):
        if yellow % i == 0:
            num = yellow // i
            if num*2+i*2+4 == brown:
                answer.append(num+2)
                answer.append(i+2)
    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))