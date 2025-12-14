def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = [0] * bridge_length

    currentWeight = 0
    while truck_weights:
        time+=1
        currentWeight = currentWeight - queue.pop(0)

        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)
    time += bridge_length

    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))