def solution(s):

    numDic = {
        "0":"zero",
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine"
    }
    strDic = {v:k for k,v in numDic.items()}

    result = ""
    tmp = ""

    for i in range(len(s)):
        tmp += s[i]

        if tmp in numDic:
            result += tmp
            s[i+1:]
            tmp = ""

        if tmp in strDic:
            result += strDic.get(tmp)
            s[i+1:]
            tmp = ""

    return int(result)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))