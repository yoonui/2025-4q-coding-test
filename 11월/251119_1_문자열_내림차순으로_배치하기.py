def solution(s):
    arr = []

    for i in s:
        arr.append(ord(i))
    arr.sort(reverse=True)

    answer = ''
    for i in arr:
        answer += chr(i)
        
    return answer

print(solution('Zbcdefg'))