# 2차원 튜플

a = ((10, 20), (30, 40), (50, 60)) # 튜플 안에 튜플을 넣은 2차원 튜플

b = ([10, 20], [30, 40], [50, 60]) # 튜플 안에 리스트를 넣음

c = [(10, 20), (30, 40), (50, 60)] # 리스트 안에 튜플을 넣음

print(a, b, c, sep='\n')

#a[0] = (500, 600)    # 바깥쪽 튜플은 변경할 수 없음. TypeError 발생

#b[0][0] = 500        # 안쪽 리스트는 변경할 수 있음

#b[0] = (500, 600)    # 바깥쪽 튜플은 변경할 수 없음. TypeError 발생

#c[0][0] = 500        # 안쪽 튜플은 변경할 수 없음. TypeError 발생

#c[0] = (500, 600)    # 바깥쪽 리스트는 변경할 수 있음

#가독성을 높이는 출력

from pprint import pprint
pprint(a, indent=4, width=20)
