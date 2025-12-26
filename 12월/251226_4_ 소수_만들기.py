def minor(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                tmp = nums[i] + nums[j] + nums[k]
                if minor(tmp): answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))