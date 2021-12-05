def get_max_number(number_list):  # 최댓값을 저장한 변수: number_list
    number = number_list[0]
    for current_number in number_list:
        if current_number > number:
            number = current_number
    return number


def get_max_index(number_list):  # 최댓값을 저장한 변수: number_list
    number = number_list[0]
    index = 0
    max_index = 0
    for index, current_number in enumerate(number_list): #enumerate로 자동으로 값을 생성함
        if current_number > number:
            number = current_number
            max_index = index
    return max_index


numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(get_max_number(numbers))  # 92
print(get_max_index(numbers))  # 1
