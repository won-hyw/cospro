def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total

def solution(total, arr):
    result = []
    req_total = func_a(arr)
    for i in arr:
        if req_total > total:
            result.append(total // len(arr))
        else:
            result.append(i)
    return result


print(solution(500, [100, 110, 140, 150]))
print(solution(500, [200, 110, 140, 150]))