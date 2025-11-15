def solution(my_string, overwrite_string, s):
    
    start = my_string[0:s]
    end = my_string[s+len(overwrite_string):]

    answer = start+ overwrite_string + end
    return answer

solution('He11oWor1d','lloWorl', 2)
solution('Program29b8UYP','merS123', 7)