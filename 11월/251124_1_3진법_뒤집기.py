def solution(n):
    answer = 0
    arr = []

    while n >= 3:
        arr.append(n % 3)
        n //= 3
    arr.append(n)

    num = len(arr) - 1
    for i in arr:
        answer += i * 3 ** num
        num -= 1

    return answer

print(solution(45))
print(solution(125))
print(solution(43046721))