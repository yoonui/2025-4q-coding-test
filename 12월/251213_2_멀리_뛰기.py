def solution(n):
    arr = [0, 1, 2]

    for i in range(3, n+1):
        arr.append(arr[i-1] + arr[i-2])

    return arr[n] % 1234567

print(solution(4))
print(solution(3))
print(solution(2))
print(solution(1))