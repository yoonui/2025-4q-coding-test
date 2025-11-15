def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq == '=': return int(n >= m)
        else: return int(n > m)
    else:
        if eq == '=': return int(n <= m)
        else: return int(n < m)

print(solution('<', '=', 20, 50))
print(solution('>', '!', 41, 78))