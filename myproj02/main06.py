# 구구단 2단 만들기
def gugudan(number):
    #number = 2
    print(f"--- {number}단 ---")
    for i in range(1,10):
        print(f" {number} * {i} = {number*i}")

'''
gugudan(2)
gugudan(3)
gugudan(4)
위의 함수 호풀부를 for문 반복문으로 변경해보세요. 
'''
# 교수님 답
for number in range(2, 10):
    gugudan(number)


# 위의 코드는 함수를 정의하는 것
# 내가 쓴 답 ↓
for j in range(2, 10):
    print(gugudan(j))

