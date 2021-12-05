import pandas as pd

df = pd.read_csv("http://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values)
print(song_list)

"""
방탄소년단의 곡명만 출력해보세요.
Hint: for 루프 내에서 if 조건문을 통해, "가수"필드체크
"""

for song_dict in song_list:
    song_dict["title"]


"""
곡명에 "가을"이 들어가는 곡명만 출력해보세요.
Hint: 포함여부 = "가을" in 곡명
"""
for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])

"""
좋아요 수가 200000이 넘는 곡수는?
Hint: int(좋아요) > 200000
가수 별 곡수를 출력해보세요.
"""
song_count = 0
for song_dict in song_list:
    if "가을" in song_dict["like"] > 200_000:
        song_count += 1
print(f"좋아요가 200,000이 넘는 곡은 {song_count} 곡입니다.")


"""
가수 별 곡수를 출력해보세요.
"""
# # artist_dict = []
# # for song_dict in song_list:
# #     artist: str = song_dict["artist"]
# #     if artist not in artist_dict:
# #         artist_dict[artist] = 0
# #     artist_dict[aritst] += 1


# print(artist_dict)

# artist_list = []
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     artist_list.append(artist)

# print(Counter(artist_list))

artist_list = [
#append되는 대상(song_dict["artist"])을 앞에 붙이고 []를 앞 뒤에 붙임 
   song_dict["artist"] for song_dict in song_list] :

print(Counter(artist_list))