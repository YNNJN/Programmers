#크롤링 하면서 알게된 find() 이용
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        temp = ''
        flag = True

        for s in skill_tree:
            if skill.find(s) != -1:
                temp += s
        for i in range(len(temp)):
            if temp[i] != skill[i]:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt

#for-else문을 이용한 풀이도 가능
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer
