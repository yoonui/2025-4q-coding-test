def minor(num):
    if num == 2:
        return True
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0

    for i in range(2, n+1):
        if minor(i): answer += 1

    return answer

print(solution(10))
print(solution(5))