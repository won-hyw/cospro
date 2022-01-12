def solution(characters):                       # "senteeeencccccceeee"
    result = [characters[0]]                    # ["s"]
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:    # "s" != "e"
            result.append(characters[i])        # result.append("e") -> result : ["s", "e"]
    return ''.join(result)

print(solution("senteeeencccccceeee"))