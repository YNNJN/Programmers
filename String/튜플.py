def solution(s):
    answer = []
    string = s[1:-1].replace('},', '}-').split('-')
    string = sorted([ele[1:-1] for ele in string], key=lambda ele: len(ele))

    for ele in string:
        for num in ele.split(","):
            if int(num) not in answer:
                answer.append(int(num))

    return answer