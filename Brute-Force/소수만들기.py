def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def solution(nums):
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                answer.append(nums[i] + nums[j] + nums[k])
    cnt = 0
    for ans in answer:
        if is_prime(ans):
            cnt += 1
    return cnt