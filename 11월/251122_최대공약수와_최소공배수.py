def solution(n, m):
    answer = []
    result = []

    i = 2
    while i <= max(n, m):
        if n % i == 0 and m % i == 0:
            result.append(i)
            n //= i
            m //= i
            i = 2
        else: i+=1
    
    num = 1    
    for i in result:
        num *= i

    answer.append(num)
    answer.append(num * n * m)
    return answer

print(solution(3, 12))
print(solution(2, 5))