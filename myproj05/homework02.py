"""
오늘의 과제 02 :  분당 타이핑 속도를 알려주도록 개선해보세요.
"""


import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비되셨으면, 엔터키를 입력해주세요.")

begin_time = time.time()
ok_count = 0
typing_counter = 0
for count in range(5):
    random_name = random.choice(animal_names)
    print(random_name)
    line = input(">>>")
    if line == random_name:
        ok_count += 1
        typing_counter += len(animal_names)
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()
typing_speed = typing_counter * 60 // (end_time - begin_time)  # // 몫만 취하기

print(f"총{ok_count}번 성공하셨습니다.")
print(f"총 {end_time - begin_time}초가 걸리셨어요.")
print(f"타이핑 속도는 {typing_speed}")

# (end_time - begin_time) : typing_counter = 60 : D **비례식 사용하기
