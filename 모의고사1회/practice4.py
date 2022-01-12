def solution(price, grade):
    global rate
    if grade == 'S':
        rate = 5
    elif grade == 'G':
        rate = 10
    elif grade == 'V':
        rate = 15
    answer = price * (1 + rate/100) # 1000 x (1 + rate / 100)
    return int(answer)

print(solution(1000, "S"))

def solution_2(price, grade):
    answer = 0
    if grade == 'S':
        answer = price + (price * 0.05)
    elif grade == 'G':
        answer = price + (price * 0.1)
    elif grade == 'V':
        answer = price + (price * 0.15)
    return int(answer)

print(solution_2(1000, "S"))