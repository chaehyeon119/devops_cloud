answer = input("12 + 23 = ") # "" 안에 들어가는 문자는 안내 메시지라고 생각하면 됨

# answer를 가지고 계산할 목적이라면,
# answer 값 변환은 최대한 빠르게 수행하는 것이 좋습니다.

answer = int(answer)

if answer == 35:
    print("정답")
else:
    print("땡!!!")