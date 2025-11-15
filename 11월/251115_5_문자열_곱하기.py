def solution(my_string, k):
    answer = ''

    for i in range(0,k):
        answer += my_string

    return answer

solution('string', 3)
solution('love', 10)