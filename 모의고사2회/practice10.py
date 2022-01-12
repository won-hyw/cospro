def sum_isbn(isbn):
    sum = 0
    for i in range(len(isbn)):  # i : 0 ~ isbn 마지막 인덱스
        c = int(isbn[i])        # '9' -> 9 / '7' -> 7
        if i % 2:               # 0 : False, 1 : True / i % 2 == 1
            w = 3
        else:
            w = 1
        sum += w * c
    return sum

def solution(isbn):
    answer = ''
    # 확인 숫자를 제외한 나머지 각 자리마다 곱한 값을 더한 총합을 구한다.
    isbn = isbn[:-1] # isbn[:12]
    total =  sum_isbn(isbn)
    answer = 10 - (total % 10)
    if answer == 10: # answer %= 10
        answer = 0
    return answer


def solution_2(isbn):
    answer = ''
    total = sum_isbn(isbn[:len(isbn) - 1])
    answer = 10 - (total % 10)
    if answer == 10:
        answer = 0
    return answer


print(solution('9788960777330'))
print(solution_2('9788960777330'))
