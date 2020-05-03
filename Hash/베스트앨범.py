#get(x, '디폴트 값') 함수는 x라는 Key에 대응되는 Value를 돌려줌


def solution(genres, plays):
    answer = []
    num = {}  #{장르 : 총 재생 횟수}
    album = {}  #{장르 : [(플레이 횟수, 고유번호)]}

    for i in range(len(genres)):
        num[genres[i]] = num.get(genres[i], 0) + plays[i]
        album[genres[i]] = album.get(genres[i], []) + [(plays[i], i)]

    genreSort = sorted(num.items(), key=lambda x: x[1], reverse=True)

    for (genre, totalPlay) in genreSort:
        album[genre] = sorted(album[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in album[genre][:2]]  # 최대 2개의 고유번호

    return answer