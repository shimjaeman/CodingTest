import re
def solution(skill, skill_trees):
    answer = 0
    new_skill_trees = [re.sub(f"[^{skill}]+", "", skill_trees[i]) for i in range(len(skill_trees))]
    for i in range(len(new_skill_trees)):        
        cnt = 0
        Flag = True
        for j in range(len(new_skill_trees[i])):
            if new_skill_trees[i][j] == skill[cnt]:
                cnt += 1
            else :
                Flag = False
                break
        if Flag :
            answer +=1
                    
            
    return answer