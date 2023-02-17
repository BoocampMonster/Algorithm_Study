string = input()
stack = []
score = 0
ratio = 1 # 이 비율에 따라 점수를 계산

for idx in range(len(string)):
    if string[idx] == '(': # 여는 괄호인 경우
        ratio *= 2     
        stack.append(string[idx])
    elif string[idx] == '[': # 여는 괄호인 경우
        ratio *= 3
        stack.append(string[idx])
    elif string[idx] == ')': # 닫는 괄호인 경우
        if not stack: # 스택이 비어 있으면 에러
            print(0)
            exit(0)
        # 다른 종류의 괄호를 만나도 에러
        elif stack and stack[-1] == '[':
            print(0)
            exit(0)
        else: # 올바른 괄호쌍인 경우
            stack.pop()
            # 직전 괄호가 닫는 것이면 점수를 추가하지 않음
            if string[idx-1] == ']' or string[idx-1] == ')':
                ratio //= 2
            else: # 직전 괄호가 여는 것이라면 점수를 추가
                score += ratio                    
                ratio //= 2
    else: # 닫는 괄호인 경우
        if not stack: # 스택이 비어 있으면 에러
            print(0)
            exit(0)
        # 다른 종류의 괄호를 만나도 에러
        elif stack and stack[-1] == '(':
            print(0)
            exit(0)
        else: # 올바른 괄호쌍인 경우
            stack.pop()
            # 직전 괄호가 닫는 것이면 점수를 추가하지 않음
            if string[idx-1] == ']' or string[idx-1] == ')':
                ratio //= 3
            else: # 직전 괄호가 여는 것이라면 점수를 추가
                score += ratio                    
                ratio //= 3
if stack: # 스택이 비어있지 않으면 올바른 괄호쌍이 아님
    print(0)
else: print(score)