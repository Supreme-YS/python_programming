# quiz_review

# 표준 입력으로 정수가 입력됩니다. range의 시작하는 숫자는 -10, 끝나는 숫자는 10이며 입력된 정수만큼 증가하는 숫자가 들어가도록 튜플을 만들고, 해당 튜플을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

term = int(input())
range_tuple = tuple(range(-10, 10, term))
print(range_tuple)
