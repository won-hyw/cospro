def solution(sentence):
    filtered = []
    for s in sentence:
        if s != ' ' and s != '.':
            filtered.append(s)
    before = sentence.replace(" ", "")
    filtered.reverse()
    after = ''.join(filtered)
    return before == after

def solution_2(sentence):
    filtered = []
    for s in sentence:
        if s != ' ' and s != '.':
            filtered.append(s)
    before = ''.join(filtered)
    filtered.reverse()
    after = ''.join(filtered)
    return before == after


print(solution_2("never odd or even"))
