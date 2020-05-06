import itertools


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    n = len(numbers)
    cnt = 0

    permu = []
    for i in range(1, n + 1):
        p_list = itertools.permutations(numbers, i)
        for p in p_list:
            permu.append(p)

    possible = []
    for ele in permu:
        x = ''.join(ele)
        possible.append(int(x))

    for ele in set(possible):
        if is_prime(ele):
            cnt += 1

    return cnt