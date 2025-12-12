def solution(s):
    listStr = s.split(' ')
    arr = []

    for i in listStr:
        if len(i) == 0: arr.append('')
        else:
            tmp = i[0].upper() + i[1:].lower()
            arr.append(tmp)

    return ' '.join(arr)

# print(solution("3people unFollowed me"))
# print(solution("for the last week"))
print(solution("  for the what  1what  "))