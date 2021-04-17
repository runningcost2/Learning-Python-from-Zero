# 자료구조의 변경
# 커피숍

menu = {"커피", "우유", "주스"} #중괄호를 이용한 집합이기때문에 class'set'으로 분류됨
print(menu, type(menu))

menu = list(menu) #list로 class를 바꿈
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)

print(menu, type(menu))