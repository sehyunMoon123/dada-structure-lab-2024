# 프로젝트 문제 2번


def problem2(input2):
    """
    제일 처음 열린 괄호는 닫힐 때까지 기다려야 하고 닫는 괄호는 여는 괄호의 역순으로 나타나므로 stack
    '('인 경우 stack에 추가하고 
    ')'인 경우 
    stack에 요소가 있고 가장 마지막 요소가 '('라면 '('와 ')'가 짝을 이루므로 '('를 stack에서 제거
    위 경우가 아니라면 ')'를 stack에 추가
    stack에 남은 괄호의 개수가 올바른 괄호열을 만들기 위해 필요한 괄호의 최소 개수
    """
   
    stack = []      
    
    for char in input2:
        if char == '(':     
            stack.append(char)     
        elif char == ')':     
            if stack and stack[-1] == '(':      
                stack.pop()     
            else:
                stack.append(char)     

    
    result = len(stack)    
    return result


# 입력받기
while True:
    input2 = input("괄호열을 입력하세요: ")
    if 1 <= len(input2) <= 50:  
        break
    else:  # 입력이 조건에 맞지 않는 경우
        print("괄호열의 길이는 1 이상 50 이하입니다.")  


# 결과 출력
result = problem2(input2)

print(result)
