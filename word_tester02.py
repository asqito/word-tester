# v0.2 개선사항
# 문제 출제 부분 함수화 : word_tester
# 입력 받을 때 숫자 외에는 받지 않도록 함수화 : integer_input
import pandas as pd


def word_tester(start, last):
    # 점수
    score = 0
    t_score = last - start + 1
    word_cnt = 1

    # 변수 first = 시작 단어, last = 끝 단어
    while start <= last:

        print(word_cnt, ".", word["뜻"][start])
        answer = input(" >> 영어 단어: ")

        # 정답인 경우
        if answer == word["단어"][start]:
            print("정답입니다!")
            score += 1

        # 오답인 경우
        else:
            print("오답, 정답은 " + word["단어"][start])

        print('\n')
        start += 1
        word_cnt += 1

    # 테스트 종료
    print("당신의 점수는", "%.1f" % ((score * 100) / t_score) + "점 입니다.\n")


def integer_input(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except ValueError:
            print("\n 1일부터 30일 중에서 날짜를 입력하세요.\n")
    return n


# 파일 불러오기
word = pd.read_excel('English_words.xlsx', sheet_name='words')

# 테스트 Day 선택하기
while True:
    day_no = integer_input("영어 단어 연습할 Day를 선택해 주세요(학습을 종료하려면 99를 입력해주세요): ")

    if day_no == 1:
        print("\n선택하신 날짜는: ", day_no, "일\n")
        s = 0
        # l = 29
        l = 9
        word_tester(s, l)

    elif 1 < day_no <= 30:
        print("\n선택하신 날짜는: ", day_no, "일\n")
        s = 0
        s += 10 * (day_no - 1)
        # 10은 30으로 변경(단어개수)
        l = s + 9
        # 9에서 29로 변경(단어개수 고려)
        word_tester(s, l)

    elif day_no == 99:
        print("\n 수고하셨습니다. \n 학습을 종료합니다.")
        break

    else:
        print("\n날짜를 잘못 선택했습니다. ", day_no)
