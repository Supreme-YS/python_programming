# formatting 

a = '{0:0<10}'.format(15)    # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움

b = '{0:0>10}'.format(15)    # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움

c = '{0:0>10.2f}'.format(15)    # 길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2자리

d = '{0: >10}'.format(15)    # 남는 공간을 공백으로 채움

e = '{0:>10}'.format(15)     # 채우기 부분을 생략하면 공백이 들어감

f = '{0:x>10}'.format(15)    # 남는 공간을 문자 x로 채움

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
