def solution(nums):
    n = int(len(nums) / 2)

    set_arr = set(nums)
    list_arr = list(set_arr)

    answer = n if n < len(list_arr) else len(list_arr)
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))