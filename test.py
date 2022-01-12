scores = [10, 3, 20, 50]

# 1. 숫자가 들어있는 리스트의 합계

def sum_list(scores):
    result = 0
    for score in scores:
        result += score
    return result

print(sum_list(scores))

# 2. 최댓값

def max_list(scores):
    max_num = scores[0]
    for score in scores:
        if max_num < score:
            max_num = score
    return max_num

print(max_list(scores))

# 3. 최솟값

def min_list(scores):
    min_num = scores[0]
    for score in scores:
        if min_num > score:
            min_num = score
    return min_num

print(min_list(scores))

# 4. 평균

def avg_list(scores):
    temp = 0
    for score in scores:
        temp += score
    result = temp / len(scores)
    return result

print(avg_list(scores))

# 5. 짝수인 것만 세기

def count_even(scores):
    result = 0
    for score in scores:
        if score % 2 == 0:
            result += 1
    return result

print(count_even(scores))

# 5. N개의 0을 가진 리스트 만들기

def make_list(n):
    result = [0 for _ in range(n)]
    return result

print(make_list(6))