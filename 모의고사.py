def solution(answers):
    score = [0 for _ in range(3)]
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == ans1[i % len(ans1)]:
            score[0] += 1
        if answers[i] == ans2[i % len(ans2)]:
            score[1] += 1
        if answers[i] == ans3[i % len(ans3)]:
            score[2] += 1

    answer = []
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i + 1)

    return answer