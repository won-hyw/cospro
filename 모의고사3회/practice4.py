def solution(walls):
    answer = 0
    painted_walls = 0
    hour = 1
    while painted_walls < walls:
        painted_walls = (hour) + (hour) + (hour)
        hour += 1
    answer = hour
    return answer

print(solution(100))