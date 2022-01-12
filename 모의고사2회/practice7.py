def solution(s):
    answer = []
    for c in s:
        if '0' <= c <= '9':
            n = ord(c) - ord('i')
            c = chr(-n)
        answer.append(c)
    return ''.join(answer)

def solution_2(s):
    answer = []
    for c in s:
        if '0' <= c <= '9': # a b 1
            n = ord('i')- ord(c)  # ord : 문자 -> ASCII코드, 숫자보다 영어가 더 큰 수
            c = chr(n)            # chr : ASCII코드 -> 문자
        answer.append(c)
    return ''.join(answer)

print(solution('ab1c3d'))



'''
print(ord('0')) # 48
print(chr(48)) # '0'
'''