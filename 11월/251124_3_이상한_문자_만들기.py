def solution(s):
    result = []
    str = ''

    arr = s.split(' ')

    for i in arr:
        if i == '': result.append(i)
        else:
            for j in range(len(i)):
                if j % 2 == 0: str += i[j].upper()
                else: str += i[j].lower()
            result.append(str)
            str = ''

    return ' '.join(result)

print(solution('try hello world'))
print(solution(' read the explanation carefully  '))