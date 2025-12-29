def solution(babbling):
    answer = 0

    for i in babbling:
        tmp = i
        len2 = i[0:2]
        stack = [0]

        while tmp:
            len2 = tmp[0:2]
            len3 = tmp[0:3]
            
            if len2 in ["ye", "ma"]:
                if stack.pop() == len2: break
                stack.append(len2)
                tmp = tmp[2:]
            elif len3 in ["aya", "woo"]:
                if stack.pop() == len3: break
                stack.append(len3)
                tmp = tmp[3:]
            else: break

        if len(tmp) == 0:
            answer += 1

    return answer

print(solution(["aya", "yee", "u"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution(["yeayaye", "wooaya", "ayayemaaya", "wooyewoo", "ayayeayayeaya", "wooyemawooye", "yemayemayema"]))
print(solution(["mama", "yeye", "woowoo", "ayaaya"]))