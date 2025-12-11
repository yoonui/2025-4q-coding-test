import datetime

def solution(a, b):
    d = datetime.datetime(2016, a, b)
    dateStr = d.strftime("%c")
    answer = dateStr[:3].upper()
    return answer

print(solution(5, 24))