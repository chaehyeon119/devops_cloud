def calculate_sum(max_number):
    accmulator = 0 # 누적할 변수 #곱하기 함수를 만든다면 초기값은 1
    for i in range(1, max_number+1):
        accmulator += i
    return accmulator

print(calculate_sum(100))