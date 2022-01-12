def solution(name_list):
    answer = 0
    for name in name_list:
        for char in name:
            if char.find('A') != -1 or char.find('K') != -1: # find()는 해당 문자가 있는 index를 반환해주므로 if문에서는 .-1인지 아닌지를 판단해줘야 한다
                answer += 1
                break
    return answer

'''
True : 100, 'a', ['a', 'b']
False : 0, '', []
'''

print(solution(['Kickboard Association','Common Engineering', 'Adios', 'CafeMasita. Ltd']))
