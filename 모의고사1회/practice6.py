def solution(left_rings):
    answer = 0
    for i in range(len(left_rings)): # i : 왼쪽고리 번호, left_rings[i] : 오른쪽고리 번호
        if left_rings[i] <= i: # 왼쪽 / 오른쪽 또는 왼쪽 - 오른쪽
            for k in range(i):
                if left_rings[k] > left_rings[i]: # 왼쪽 \ 오른쪽
                    answer += 1
    return answer

print(solution([0, 3, 1, 4, 2])) # 3
print(solution([1, 2, 3, 4, 5])) # 0
print(solution([2, 4, 0, 3, 1])) # 6
print(solution([3, 1, 2, 4, 0])) # 6

