def solution(array, commands):
    answer = []
    for ele in commands:
        temp = array[ele[0]-1: ele[1]]
        temp.sort()
        answer.append(temp[ele[2]-1])
    return answer