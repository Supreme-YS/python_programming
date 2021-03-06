#핵심 정리

#반복할 횟수를 지정하여 반복하기
for 변수 in range(횟수):
    반복할 코드

#반복할 횟수가 정해져 있지 않을 때 반복하기

초기식

while 조건식 :
    반복할 코드
    조건식의 결과에 영향을 주는 코드(변화식)

#반복문 끝내기

while 조건식1:
    if 조건식2:
        break #반복문을 끝냄

#반복문의 코드 건너뛰기

while 조건식1:
    if 조건식2:
        continue #아래 코드를 건너뛴 뒤 계속 반복함
    코드

#중첩루프

for i in range(10): #바깥쪽 루프
    for j in range(10): #안쪽 루프
        pass

#반복문과 들여쓰기

#for while 다음에 오는 코드는 반드시 들여쓰기를 해야하고 깊이가 같아야 한다.
