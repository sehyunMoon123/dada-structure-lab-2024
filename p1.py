# 프로젝트 문제 1번


def problem1(input):
    """
    mean은 input의 숫자들을 더한 후 리스트의 길이, 즉 숫자 개수로 나눠 평균을 구함
    주어지는 숫자들은 모두 5의 배수이므로 평균이 자연수가 나오지 않는 경우는 고려하지 않아도 됨
    median은 리스트를 크기순으로 정렬한 후 중앙값을 구함
    주어지는 숫자가 5개이므로 숫자의 개수가 짝수개인 경우는 고려하지 않아도 됨
    """

    mean = 0
    median = 0
    result = [0, 0]

    mean = sum(input) / len(input)
    mean = int(mean)  # 평균을 정수형으로 변환

    sorted_input = sorted(input)
    median = sorted_input[2]  # 정렬된 리스트의 세 번째 값이 중앙값
    
    result[0] = mean
    result[1] = median
    return result


# 입력받기
input_numbers = []
for i in range(5):
    while True:
        try:
            number = int(input(f"{i+1}번째 자연수를 입력하세요: "))
            if number < 100 and number % 10 == 0:
                input_numbers.append(number)
                break
            else:  # 입력이 조건에 맞지 않는 경우
                print("100보다 작은 10의 배수를 입력해주세요.")
        except ValueError:  # 입력이 숫자가 아닌 경우
            print("유효한 숫자를 입력해주세요.")


# 결과 출력
result = problem1(input_numbers)

print(f"평균 : {result[0]}")  # 평균 출력
print(f"중앙값 : {result[1]}")  # 중앙값 출력
