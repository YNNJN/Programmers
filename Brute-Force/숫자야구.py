import itertools


def baseball_fun(x, y):
    x, y = list(x), list(y)
    s, b = 0, 0
    for i in range(3):
        if x[i] in y:
            if y.index(x[i]) == i:
                s += 1
            else:
                b += 1
    return [s, b]

def solution(baseball):
    question = list(map(lambda x: str(x[0]), baseball))
    answer = list(map(lambda x: [x[1], x[2]], baseball))
    all = list(itertools.permutations(range(1, 10), 3))
    all = list(map(lambda x: list(map(str, x)), all))

    cnt = 0
    for x in all:
        if [baseball_fun(x, y) for y in question] == answer: cnt += 1

    return cnt

