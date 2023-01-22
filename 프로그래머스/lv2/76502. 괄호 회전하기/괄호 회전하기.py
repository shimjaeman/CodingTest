def solution(s):
    check_list = ["[]", "{}", "()"]
    answer = 0
    new_s = list(s)
    # 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전을 위한 for문
    for _ in range(len(new_s)):
        stack = []
        index = 0
        for j in range(len(new_s)):
            stack.append(new_s[j])
            index += 1
            # 두개의 괄호 문자가 들어온 경우
            if index >= 2:
                # 2개의 괄호가 올바른 괄호인경우 
                if stack[index-2] + stack[index-1] in check_list:
                    del stack[index-1]
                    del stack[index-2]
                    index = len(stack)
        
        # 모든 괄호가 제거된 경우
        if not stack:
            answer +=1
             
        # 왼쪽으로 1칸씩 회전
        rot = new_s[0]
        del new_s[0]
        new_s.append(rot)
        
    return answer