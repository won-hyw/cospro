def solution(weight, k):
    answer = 0
    for w in weight:
        if w > k:
            answer += 1
    return answer

print(solution([65, 70, 75, 80, 84], 75))
print(solution([65, 70, 75, 80, 84], 74))