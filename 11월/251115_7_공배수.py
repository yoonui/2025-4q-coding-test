def solution(number, n, m):
    answer = 1 if number % n == 0 and number % m == 0 else 0
    return answer

solution(60, 2, 3)
solution(55, 10, 5)