"""
랜덤 숫자를 맞춰보세요.
hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.
유저에게 10회의 기회를 줍니다.
 - 그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는 지 출력
 - 입력한 숫자가 랜덤수보다 작다면, "더 큰 수를 입력해주세요." 라고 출력
 - 입력한 숫자가 랜덤수보다 크다면, "더 작은 수를 입력해주세요."라고 출력
 - 횟수를 초과했다면, "다음 기회에 ..." 라고 출력
"""

from random import randint

number = randint(1, 100)

# 10번의 기회를 주니까
for retry in range(1, 11):
    # ↓ 대괄호는 아무 의미없음 출력용임
    line = input(f"[{retry}]Try guess number : ")
    # 문자열 앞에 스페이스가 들어갈 수도 있으니 strip으로 제거
    try:
        answer = int(line.strip())
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
        continue # 바로 위로 올라감 아래 코드를 실행하지 않음 retry가 1이었다면 continue를 만나 retry가 2가됨

    if answer == number:
        print(f"{retry}회 시도에 성공.")
        break
    elif answer < number:
        print("더 큰 수를 입력해주세요.")
    # elif answer > number:
    else:
        print("더 작은 수를 입력해주세요")
# 횟수를 다 채우고 정상적으로 수행되면 아래 else가 수행됨
# 중간에 break를 만나면 수행은 안됨
else:
    print("다음 기회에...")
