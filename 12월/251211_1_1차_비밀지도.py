def solution(n, arr1, arr2):
    answer = []

    two1 = []
    two2 = []

    for i in arr1:
        tmp = str(bin(i))[2:]
        two1.append(tmp.zfill(n))
    
    for i in arr2:
        tmp = str(bin(i))[2:]
        two2.append(tmp.zfill(n))
    
    for i in range(n):
        tmp = ""
        for j in range(n):
            if two1[i][j] == "1" or two2[i][j] == "1":
                tmp += "#"
            else: tmp+= " "
        answer.append(tmp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))