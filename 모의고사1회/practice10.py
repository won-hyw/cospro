def solution(data):
    total = 0
    for i in data:
        total += i
    cnt = 0
    average = total // len(data)
    for i in data:
        if i < average:
            cnt += 1
    return cnt

data = [i for i in range(1, 11)]
print(solution(data))