# 튜플은 변화가 없는 리스트를 의미

menu = ("돈까스", "치즈까스") #무조건 돈까스와 치즈까스만 파는 가게
print(menu[0])
print(menu[1])

# menu.add("생선까스") #해보면 에러뜸

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)  #원래는 하나하나 선언해줘야함

(name, age, hobby) = ("김종국", 20, "코딩") #튜플을 이용하면 한번에 선언 가능
print(name, age, hobby)