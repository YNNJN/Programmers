def solution(participant, completion):
    completion.append('z'*10)
    for p,c in zip(sorted(participant), sorted(completion)):
        if p != c:
            return p