def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            cards1 = cards1[1:]
            continue
        elif len(cards2) > 0 and i == cards2[0]:
            cards2 = cards2[1:]
            continue
        else: return "No"
    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"]))