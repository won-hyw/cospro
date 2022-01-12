def solution(shoes_size) :
    answer = [0 for _ in range(len(shoes_size))]        # count를 세기 위한 변수 초기화
    for size in shoes_size:
        if size == '7':
            answer[0] += 1
        elif size == '7.5':
            answer[1] += 1
        elif size == '8':
            answer[2] += 1
        elif size == '8.5':
            answer[3] += 1
        elif size == '9':
            answer[4] += 1
        elif size == '9.5':
            answer[5] += 1
    return answer


print(solution(['7', '9', '7', '8.5', '8', '7']))