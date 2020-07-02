import pandas as pd

# 파일에서 'words' 시트 불러오기
word = pd.read_excel('English_words01.xlsx', sheet_name='words')

# 테스트 Day 선택하기
day_no = input('단어 연습할 Day를 선택해 주세요:')

# 점수 초기화
score = 0

# 테스트 페이지 선택하기
# 단어는 10개씩 테스트
if day_no == "1":
    j = 0
    k = 9

elif day_no == "2":
    j = 10
    k = 19

elif page_no == "3":
    j = 20
    k = 29

# 테스트
while j <= k:

    # 엑셀 파일에서 불러온 'words'시트에서 뜻 column을 불러와서 문제
    print(word['뜻'][j])
    answer = input(" >> 영어 단어: ")

    # 정답인 경우
    if answer == word['단어'][j]:
        print("정답입니다!")
        score += 1

    # 오답인 경우
    else:
        print("오답, 정답은 " + word['단어'][j])

    print("\n")
    j += 1

# 테스트 종료
print("당신의 점수는", "%.1f" % ((score * 100) / (k + 1)) + "점 입니다.")
