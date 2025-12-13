from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        time = 0
        frist = queue.popleft()

        for i in queue:
            time+=1
            if frist > i:
                break
        answer.append(time)

    return answer

print(solution([1, 2, 3, 2, 3]))