def solution(n, price):                     # N : 대회에 참가하는 팀 수 / PRICE : 축구장의 하루 대여료
    games = n * (n - 1) // 2                # 리그 전의 경기의 수
    per_day = n // 2                        # 하루에 진행할 수 있는 경기의 수
    answer = (games // per_day) * price
    return answer                           # RETURN값 임대료

print(solution(2, 1000))