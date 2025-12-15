def solution(n):
    oneCount = bin(n).count("1")
    tmp = n+1

    while True:
        if bin(tmp).count("1") == oneCount:
            return tmp
        else: tmp += 1


print(solution(78))
print(solution(15))