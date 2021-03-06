"""
짝수만 뽑기
"""

# def check_even_number(number):
#     return number % 2 == 0

# numbers = [0,1,2,3,4,5,6,7,8,9]

# for number in filter(check_even_number, numbers):
#     print(number)

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

print("===방탄소년단 곡명만 출력하기===")


def filter_fn1(song_dict):
    return song_dict["artist"] == "방탄소년단"


for song_dict in filter(filter_fn1, song_list):
    print(song_dict["title"])

print("===곡명에 '사랑'이 포함된 곡명만 출력하기===")


def filter_fn2(song_dict):
    return "사랑" in song_dict["title"]


for song_dict in filter(filter_fn2, song_list):
    print(song_dict["title"])


print("===좋아요 수가 200,000이상인 곡명만 출력하기===")


def filter_fn3(song_dict):
    return song_dict["like"] > 200_000


for song_dict in filter(filter_fn3, song_list):
    print(song_dict["like"], song_dict["title"])


print("===좋아요 수가 200,000이상인 곡에 대해서, 곡명 가나다 순으로 정렬===")
# 곡명에 대한 오름차순 문제
# 1안) 필러팅을 먼저하고, 필터링된 결과에 대해서 곡명 오름차순 정렬(!!!!)
# 2안) 곡명에 대한 오름차순 정렬을 먼저하고, 필터링
# 1안이 더 나음. 필터링을 먼저해서 모수를 먼저 줄이고 정렬하는 것이 더 나음


def filter_fn4(song_dict):
    return song_dict["like"] > 200_000


def sort_fn4(song_dict):
    return song_dict["title"]


new_song_list = filter(filter_fn4, song_list)  # list 타입은 아닙니다.
new_song_list = sorted(new_song_list, key=sort_fn4)

sorted(new_song_list, key=sort_fn4)

for song_dict in new_song_list:
    print(song_dict["like"], song_dict["title"])
