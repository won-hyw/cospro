def solution(orders): # ORDERS = [[0, 0, 4, 0, 0, 1]]
    answer = 0
    size = 0
    for o in orders: # [0, 0, 4, 0, 0, 1]
        for i in range(6): # index 0 ~ 5
            if o[i] != 0: # 개수가 0이 아니면
                size += ((i + 1) ** 2) * o[i] # 3x3 + 실제 제품이 차지하는 면적
    answer = size // 36
    if size % 36 != 0:
        answer += 1
    return answer

print(solution([[0, 0, 4, 0, 0, 1]]))