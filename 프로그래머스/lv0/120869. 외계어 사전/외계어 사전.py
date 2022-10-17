def solution(spell, dic):
    toge_spell = "".join(sorted(spell))
    for i in dic:
        i = "".join(sorted(i))
        if i.find(toge_spell) != -1:
            return 1
        else :
            continue
        
    return 2
            
            