def solution(food):
    result = []

    for i in range(len(food)):
        num = food[i] // 2
        if num > 0:
            for j in range(num):
                result.append(str(i))

    non_str = ''.join(result)
    reverse_str = ''.join(reversed(result))

    return non_str+'0'+reverse_str

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))